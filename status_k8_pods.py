import pandas as pd
import matplotlib.pyplot as plt
import json

# Read CSV file into DataFrame
csv_file = 'status_k8_pod_containers_exported_06_03_2024.csv'  # Replace with your actual file path
df = pd.read_csv(csv_file)

# Convert 'container_started_at' to datetime
df['container_started_at'] = pd.to_datetime(df['container_started_at'], errors='coerce')

# Format 'container_started_at' to 'YYYY-MM-DD HH:MM:SS'
df['container_started_at'] = df['container_started_at'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Replace NaN with "empty"
df.fillna("empty", inplace=True)

# Extract information from 'container_state_msg' column
def parse_state_msg(state_msg):
    if state_msg == "empty":
        return {"reason": "empty", "signal": "empty", "message": "empty", "exit_code": "empty", "started_at": "empty", "finished_at": "empty", "container_id": "empty"}
    try:
        return json.loads(state_msg)
    except ValueError:
        return {"reason": "invalid", "signal": "invalid", "message": "invalid", "exit_code": "invalid", "started_at": "invalid", "finished_at": "invalid", "container_id": "invalid"}

parsed_msgs = df['container_state_msg'].apply(parse_state_msg)
parsed_df = pd.json_normalize(parsed_msgs)

# Merge extracted information with the original DataFrame
df = df.join(parsed_df)

# Calculate the age in days for each container
df['container_started_at'] = pd.to_datetime(df['container_started_at'], errors='coerce')
df['age_in_days'] = (pd.to_datetime('today') - df['container_started_at']).dt.days

# Extract image name and version
df['image_name'] = df['container_images'].apply(lambda x: x.strip('[]').split('/')[-1].split(':')[0])
df['image_version'] = df['container_images'].apply(lambda x: x.strip('[]').split(':')[-1])

# Summary DataFrame
df_summary = df[['container_name', 'pod_name', 'namespace', 'cluster_name', 'image_name', 'image_version', 'container_state', 'age_in_days', 'reason', 'message']]

# Save the summary DataFrame as a CSV file
df_summary.to_csv('summary_pod_containers.csv', index=False)

# Analysis 1: Count of Containers by Namespace
containers_by_namespace = df['namespace'].value_counts().reset_index()
containers_by_namespace.columns = ['namespace', 'count']
containers_by_namespace.to_csv('containers_by_namespace.csv', index=False)

# Analysis 2: Count of Containers by Cluster Name
containers_by_cluster = df['cluster_name'].value_counts().reset_index()
containers_by_cluster.columns = ['cluster_name', 'count']
containers_by_cluster.to_csv('containers_by_cluster.csv', index=False)

# Analysis 3: Containers by State
containers_by_state = df['container_state'].value_counts().reset_index()
containers_by_state.columns = ['container_state', 'count']
containers_by_state.to_csv('containers_by_state.csv', index=False)

# Analysis 4: Age of Containers in Days
containers_age = df[['container_name', 'pod_name', 'namespace', 'cluster_name', 'age_in_days']].sort_values(by='age_in_days', ascending=False)
containers_age.to_csv('containers_age_analysis.csv', index=False)

# Analysis 5: Containers by Name, State, State Message, Image Name, and Version
containers_detail = df[['container_name', 'container_state', 'reason', 'message', 'image_name', 'image_version']]
containers_detail.to_csv('containers_detail_analysis.csv', index=False)

# Display DataFrames in nicely formatted tables using pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

# Print the nicely formatted DataFrames
print("\nSummary DataFrame:")
print(df_summary.to_string(index=False))

print("\nContainers by Namespace:")
print(containers_by_namespace.to_string(index=False))

print("\nContainers by Cluster:")
print(containers_by_cluster.to_string(index=False))

print("\nContainers by State:")
print(containers_by_state.to_string(index=False))

print("\nContainers Age Analysis:")
print(containers_age.to_string(index=False))

print("\nContainers Detail Analysis:")
print(containers_detail.to_string(index=False))
