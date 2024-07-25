import pandas as pd
import boto3
import requests
import io
import json
import base64
import re

# Initialize S3 client
s3 = boto3.client('s3')

# Confluence API details
confluence_base_url = 'https://sentinelone.atlassian.net/wiki/rest/api/content'
confluence_username = 'priemail.com'
confluence_api_token = 'ttoken'
confluence_page_id = '3733356828'  # Specific page ID to update

def lambda_handler(event, context):
    # Bucket and paths
    bucket = 'cerebro-reports-confluence'
    input_prefix = 'input/'
    output_prefix = 'output/'

    try:
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

                # Format each report
                kubernetes_report = format_kubernetes_deployments_report(max_age_df)
                summary_report = format_summary_report(df)

                # Prepare new content with section headers
                new_content = f"""
                <h3 style="color:#2c3e50;">Kubernetes Deployments Analysis</h3>
                {kubernetes_report}
                <h3 style="color:#2c3e50;">Summary of Kubernetes Deployments</h3>
                {summary_report}
                """

                # Fetch current page content and version
                current_content, current_version = get_current_page_content(confluence_page_id)

                # Clean old content and insert new content
                updated_content = clean_and_insert_content(current_content, new_content)

                # Push updated content to Confluence
                push_to_confluence(updated_content, current_version)

        return {
            'statusCode': 200,
            'body': json.dumps('Reports generated, pushed to Confluence, and saved to S3')
        }
    except Exception as e:
        print(f"Exception encountered: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Failed: {str(e)}')
        }

def save_csv_to_s3(df, s3_key):
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket='cerebro-reports-confluence', Key=s3_key, Body=csv_buffer.getvalue())

def push_to_confluence(content, current_version):
    url = f"{confluence_base_url}/{confluence_page_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {base64.b64encode(f"{confluence_username}:{confluence_api_token}".encode()).decode()}'
    }

    # Prepare data payload for update
    data = {
        'version': {
            'number': current_version + 1
        },
        'title': 'Kubernetes Deployment Reports',
        'type': 'page',
        'body': {
            'storage': {
                'value': content,
                'representation': 'storage'
            }
        }
    }

    # Make the PUT request to update the page content
    response = requests.put(url, headers=headers, data=json.dumps(data))

    # Detailed logging
    print(f"Request URL: {url}")
    print(f"Request Headers: {headers}")
    print(f"Request Data: {json.dumps(data, indent=2)}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

    if response.status_code == 200:
        print("Successfully updated Confluence page.")
    else:
        print(f"Failed to update Confluence page. Response: {response.text}")

def get_current_page_content(page_id):
    # Function to fetch current content and version of a page
    url = f"{confluence_base_url}/{page_id}?expand=body.storage,version"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {base64.b64encode(f"{confluence_username}:{confluence_api_token}".encode()).decode()}'
    }
    response = requests.get(url, headers=headers)

    # Detailed logging
    print(f"Request URL: {url}")
    print(f"Request Headers: {headers}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

    if response.status_code == 200:
        page_data = response.json()
        current_content = page_data['body']['storage']['value']
        current_version = page_data['version']['number']
        return current_content, current_version
    else:
        raise Exception(f"Failed to fetch current content of Confluence page: {response.text}")

def clean_and_insert_content(current_content, new_content):
    # Define section titles
    section_titles = [
        'Kubernetes Deployments Analysis',
        'Summary of Kubernetes Deployments'
    ]
    
    # Remove all sections by title
    for title in section_titles:
        pattern = re.compile(f'(<h3 style="color:#2c3e50;">{re.escape(title)}</h3>.*?)(?=<h3 style="color:#2c3e50;">|$)', re.DOTALL)
        current_content = pattern.sub('', current_content).strip()

    # Insert new content
    cleaned_content = f"""
    {current_content}
    {new_content}
    """
    
    return cleaned_content

def format_kubernetes_deployments_report(df):
    # Format Kubernetes Deployments Analysis report into HTML table for Confluence
    html_content = '''
    <h3 style="color:#2c3e50;">Kubernetes Deployments Analysis</h3>
    <p>Here is a summary of Kubernetes deployments showing the maximum age in days and recommended action.</p>
    <table style="width:100%; border-collapse:collapse; border:1px solid #ddd;">
        <thead style="background-color:#f2f2f2;">
            <tr>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Owner</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Namespace</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Image Name</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Age in Days</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Action</b></th>
            </tr>
        </thead>
        <tbody>
    '''
    
    for _, row in df.iterrows():
        html_content += '<tr>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["owner"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["namespace"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["image_name"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["age_in_days"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["action"]}</td>'
        html_content += '</tr>'
    
    html_content += '''
        </tbody>
    </table>
    '''
    
    return html_content

def format_summary_report(df):
    # Format Summary of Kubernetes Deployments report into HTML table for Confluence
    html_content = '''
    <h3 style="color:#2c3e50;">Summary of Kubernetes Deployments</h3>
    <p>Here is a summary of Kubernetes deployments showing various metrics.</p>
    <table style="width:100%; border-collapse:collapse; border:1px solid #ddd;">
        <thead style="background-color:#f2f2f2;">
            <tr>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Namespace</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Owner</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Group</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Environment</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Image Name</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Creation Timestamp</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Age in Days</b></th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;"><b>Image Version</b></th>
            </tr>
        </thead>
        <tbody>
    '''
    
    for _, row in df.iterrows():
        html_content += '<tr>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["namespace"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["owner"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["group"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["environment"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["image_name"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["creation_timestamp"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["age_in_days"]}</td>'
        html_content += f'<td style="border:1px solid #ddd; padding:8px;">{row["image_version"]}</td>'
        html_content += '</tr>'
    
    html_content += '''
        </tbody>
    </table>
    '''
    
    return html_content
