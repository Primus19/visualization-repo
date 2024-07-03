import json
import boto3
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests
from datetime import datetime

# Initialize S3 client
s3 = boto3.client('s3')

# Confluence API details
confluence_base_url = 'https://your-confluence-instance.atlassian.net/wiki/rest/api'
confluence_username = 'your-confluence-username'
confluence_api_token = 'your-confluence-api-token'
confluence_space_key = 'YOUR_SPACE_KEY'
confluence_ancestor_id = 'PARENT_PAGE_ID'  # The ID of the parent page under which the new page will be created

def lambda_handler(event, context):
    # Bucket and paths
    bucket = 'cerebro-reports-confluence'
    input_prefix = 'input/'
    output_prefix = 'output/'
    
    # List all objects in the input folder
    input_files = s3.list_objects_v2(Bucket=bucket, Prefix=input_prefix)
    
    # Process each file in the input folder
    for obj in input_files.get('Contents', []):
        file_key = obj['Key']
        
        if file_key.endswith('.csv'):
            # Read CSV file from S3
            obj = s3.get_object(Bucket=bucket, Key=file_key)
            df = pd.read_csv(io.BytesIO(obj['Body'].read()))

            # Data processing
            df['creation_timestamp'] = pd.to_datetime(df['creation_timestamp'], errors='coerce')
            df['creation_timestamp'] = df['creation_timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
            df.fillna("empty", inplace=True)
            
            # Extract labels
            labels_df = df['labels'].apply(json.loads).apply(pd.Series)
            labels_df['owner'] = labels_df.get('owner', 'unknown')
            labels_df['group'] = labels_df.get('group', 'unknown')
            labels_df['environment'] = labels_df.get('environment', 'unknown')
            labels_df['image_name'] = df['spec_images'].apply(lambda x: x.strip('[]').split('/')[-1].split(':')[0])
            labels_df['image_version'] = df['spec_images'].apply(lambda x: x.strip('[]').split(':')[-1])
            
            # Merge extracted labels with original DataFrame
            df = df.join(labels_df[['owner', 'group', 'environment', 'image_name', 'image_version']])

            # Plotting
            plot_and_save(df, 'namespace', 'Count of Deployments by Namespace', f'{output_prefix}deployments_by_namespace.png', 'skyblue')
            plot_and_save(df, 'owner', 'Count of Deployments by Owner', f'{output_prefix}deployments_by_owner.png', 'lightgreen')
            plot_and_save(df, 'environment', 'Count of Images by Environment', f'{output_prefix}images_by_environment.png', 'coral')

            # Analysis
            df['creation_timestamp'] = pd.to_datetime(df['creation_timestamp'], format='%Y-%m-%d %H:%M:%S')
            df['age_in_days'] = (pd.to_datetime('today') - df['creation_timestamp']).dt.days
            max_age_df = df.groupby(['owner', 'namespace', 'image_name'])['age_in_days'].max().reset_index()
            max_age_df['action'] = max_age_df['age_in_days'].apply(lambda x: 'replace' if x > 90 else 'maintain')
            save_csv_to_s3(max_age_df, f'{output_prefix}max_age_analysis.csv')
            
            # Detailed analysis
            detailed_analysis = df.groupby(['namespace', 'owner', 'group', 'environment', 'image_name']).size().reset_index(name='count')
            save_csv_to_s3(detailed_analysis, f'{output_prefix}detailed_analysis.csv')
            
            # Additional grouping analysis
            namespace_owner_group = df.groupby(['namespace', 'owner']).size().reset_index(name='count')
            save_csv_to_s3(namespace_owner_group, f'{output_prefix}namespace_owner_analysis.csv')
            environment_image_group = df.groupby(['environment', 'image_name', 'owner', 'namespace', 'age_in_days', 'image_version']).size().reset_index(name='count')
            save_csv_to_s3(environment_image_group, f'{output_prefix}environment_image_analysis.csv')
            
            # Save summary DataFrame as a CSV file
            save_csv_to_s3(df, f'{output_prefix}summary_k8s_deployments.csv')

            # Push the report to Confluence
            push_to_confluence(df.to_string(index=False), 'K8s Deployments Summary')

    return {
        'statusCode': 200,
        'body': json.dumps('Reports generated, pushed to Confluence, and saved to S3')
    }

def plot_and_save(df, column, title, s3_key, color):
    plt.figure(figsize=(10, 6))
    df[column].value_counts().plot(kind='bar', color=color)
    plt.title(title)
    plt.xlabel(column.capitalize())
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('/tmp/plot.png', bbox_inches='tight')
    plt.close()
    save_plot_to_s3('/tmp/plot.png', s3_key)

def save_plot_to_s3(local_path, s3_key):
    bucket = 'cerebro-reports-confluence'
    with open(local_path, 'rb') as f:
        s3.put_object(Bucket=bucket, Key=s3_key, Body=f)

def save_csv_to_s3(df, s3_key):
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket='cerebro-reports-confluence', Key=s3_key, Body=csv_buffer.getvalue())

def push_to_confluence(content, title):
    url = f"{confluence_base_url}/content/"
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    data = {
        'type': 'page',
        'title': title,
        'space': {
            'key': confluence_space_key
        },
        'ancestors': [
            {
                'id': confluence_ancestor_id
            }
        ],
        'body': {
            'storage': {
                'value': f"<pre>{content}</pre>",
                'representation': 'storage'
            }
        }
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data), auth=(confluence_username, confluence_api_token))
    
    if response.status_code != 200:
        raise Exception(f"Failed to create Confluence page: {response.content}")
    
    return response.json()
