import pandas as pd
import boto3
import requests
import io
import json
import base64
import datetime

# Initialize S3 client
s3 = boto3.client('s3')

# Confluence API details
confluence_base_url = 'https://sentinelone.atlassian.net/wiki/rest/api/content'
confluence_username = 'primus.veemaelone.com'
confluence_api_token = 'toenD'
confluence_page_id = '3733356828'  # Specific page ID to update

def lambda_handler(event, context):
    bucket = 'gov-configuration-data'
    
    # Log incoming event for debugging
    print(f"Event: {json.dumps(event)}")
    
    try:
        # Extract S3 bucket and key from the event
        if 'Records' in event and len(event['Records']) > 0 and 's3' in event['Records'][0]:
            s3_record = event['Records'][0]['s3']
            bucket_name = s3_record['bucket']['name']
            key = s3_record['object']['key']
            print(f"Extracted bucket: {bucket_name}")
            print(f"Extracted key from event: {key}")
        else:
            raise ValueError("S3 event records not found in the event")

        # Adjust the key based on the current date
        current_date_folder = get_current_monday_date_folder()
        adjusted_key = key.split('/')[0] + '/' + current_date_folder + '/' + '/'.join(key.split('/')[2:])
        print(f"Adjusted key with current date: {adjusted_key}")

        # Read CSV file from S3
        try:
            obj = s3.get_object(Bucket=bucket_name, Key=adjusted_key)
            df = pd.read_csv(io.BytesIO(obj['Body'].read()))
        except s3.exceptions.NoSuchKey:
            raise Exception(f"NoSuchKey: The specified key does not exist: {adjusted_key}")

        # Log DataFrame columns for debugging
        print(f"DataFrame columns: {df.columns.tolist()}")

        # Check for required columns
        required_columns = ['container_name', 'pod_name', 'namespace', 'cluster_name', 'container_image', 'container_state', 'container_started_at', 'image_age_days', 'last_updated']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise KeyError(f"Missing required columns: {', '.join(missing_columns)}")

        # Clean and format date columns, handling possible errors
        def clean_and_format_date(column, df):
            if column not in df.columns:
                print(f"Column '{column}' is missing, skipping date processing.")
                return
            
            # Define a list of possible date formats
            date_formats = [
                "%Y-%m-%d %H:%M:%S%z",
                "%Y-%m-%d %H:%M:%S",
                "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%dT%H:%M:%S",
                "%m/%d/%Y %H:%M:%S",
                "%d-%m-%Y %H:%M:%S",
                "%Y/%m/%d %H:%M:%S",
                "%d-%b-%Y %H:%M:%S",
                "%d/%b/%Y %H:%M:%S"
            ]
            
            # Convert column to string to handle cases where it's not already a string
            df[column] = df[column].astype(str)

            # Replace empty values with NaT
            df[column] = df[column].replace(['', ' ', 'None'], pd.NaT)

            # Function to attempt parsing a date with multiple formats
            def parse_date(date_str):
                if pd.isna(date_str):
                    return pd.NaT
                for date_format in date_formats:
                    try:
                        return pd.to_datetime(date_str, format=date_format, errors='coerce')
                    except ValueError:
                        continue
                return pd.NaT  # Return Not a Time for unparseable dates
            
            # Apply the parsing function
            df[column] = df[column].apply(parse_date)

            # Check for any remaining invalid dates
            invalid_dates = df[df[column].isna()][column]
            if not invalid_dates.empty:
                invalid_dates_list = invalid_dates.unique()
                # Print invalid dates and their raw values for debugging
                print(f"Invalid dates in '{column}': {invalid_dates_list}")
                raw_invalid_entries = df[df[column].isna()][column]
                print(f"Raw invalid entries in '{column}': {raw_invalid_entries.tolist()}")
                # Optional: Drop rows with invalid dates instead of dropping the column
                # df.dropna(subset=[column], inplace=True)
                # Print message for debugging
                print(f"Skipping column '{column}' due to invalid dates.")

        # Clean and format 'container_started_at' and 'last_updated'
        clean_and_format_date('container_started_at', df)
        clean_and_format_date('last_updated', df)

        # Convert 'container_started_at' to timezone-naive if it's timezone-aware
        if 'container_started_at' in df.columns:
            df['container_started_at'] = df['container_started_at'].dt.tz_localize(None)

        # Calculate image age if 'container_started_at' is available
        if 'container_started_at' in df.columns and not df['container_started_at'].isna().all():
            today = pd.to_datetime('today').normalize()
            df['age_in_days'] = (today - df['container_started_at']).dt.days
        else:
            # Use 'image_age_days' column if 'container_started_at' is missing or invalid
            if 'image_age_days' not in df.columns:
                raise KeyError("'image_age_days' column is missing.")
            df['age_in_days'] = df['image_age_days'].astype('Int64')

        # Data processing
        max_age_df = df.groupby(['cluster_name', 'namespace', 'container_image'])['age_in_days'].max().reset_index()
        max_age_df['action'] = max_age_df['age_in_days'].apply(lambda x: 'replace' if x > 90 else 'maintain')
        save_csv_to_s3(max_age_df, 'Gov2/output/max_age_analysis.csv')

        # Detailed analysis
        detailed_analysis = df.groupby(['namespace', 'cluster_name', 'container_image']).size().reset_index(name='count')
        save_csv_to_s3(detailed_analysis, 'Gov2/output/detailed_analysis.csv')

        # Additional grouping analysis
        namespace_cluster_analysis = df.groupby(['namespace', 'cluster_name']).size().reset_index(name='count')
        save_csv_to_s3(namespace_cluster_analysis, 'Gov2/output/namespace_cluster_analysis.csv')
        age_image_analysis = df.groupby(['container_image', 'namespace', 'cluster_name', 'age_in_days']).size().reset_index(name='count')
        save_csv_to_s3(age_image_analysis, 'Gov2/output/age_image_analysis.csv')

        # Save summary DataFrame as a CSV file
        save_csv_to_s3(df, 'Gov2/output/summary_k8s_deployments.csv')

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
            'body': json.dumps('Success')
        }
    except Exception as e:
        print(f"Exception encountered: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Failed: {str(e)}')
        }

def get_current_monday_date_folder():
    today = datetime.datetime.now()
    monday = today - datetime.timedelta(days=today.weekday())
    date_folder = monday.strftime('%Y%m%d')
    return date_folder

def save_csv_to_s3(df, s3_key):
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket='gov-configuration-data', Key=s3_key, Body=csv_buffer.getvalue())
    print(f"Saved CSV to S3: {s3_key}")

def push_to_confluence(content, current_version &#8203;:citation[oaicite:0]{index=0}&#8203;
