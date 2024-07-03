import pandas as pd
import matplotlib.pyplot as plt
import json

# Read CSV file into DataFrame
csv_file = 'k8s_deployments_exported_06_03_2024.csv'
df = pd.read_csv(csv_file)

# Convert 'creation_timestamp' to datetime
df['creation_timestamp'] = pd.to_datetime(df['creation_timestamp'], errors='coerce')

# Format 'creation_timestamp' to 'YYYY-MM-DD HH:MM:SS'
df['creation_timestamp'] = df['creation_timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Replace NaN with "empty"
df.fillna("empty", inplace=True)

# Display basic information about the DataFrame
print(df.info())

# Extract relevant information from 'labels' column
labels_df = df['labels'].apply(json.loads).apply(pd.Series)
labels_df['owner'] = labels_df.get('owner', 'unknown')
labels_df['group'] = labels_df.get('group', 'unknown')
labels_df['environment'] = labels_df.get('environment', 'unknown')
labels_df['image_name'] = df['spec_images'].apply(lambda x: x.strip('[]').split('/')[-1].split(':')[0])
labels_df['image_version'] = df['spec_images'].apply(lambda x: x.strip('[]').split(':')[-1])

# Merge extracted labels with original DataFrame
df = df.join(labels_df[['owner', 'group', 'environment', 'image_name', 'image_version']])

# Plot 1: Count of Deployments by Namespace
plt.figure(figsize=(10, 6))
df['namespace'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Count of Deployments by Namespace')
plt.xlabel('Namespace')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('deployments_by_namespace.png', bbox_inches='tight')
plt.show()

# Plot 2: Count of Deployments by Owner
plt.figure(figsize=(10, 6))
df['owner'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Count of Deployments by Owner')
plt.xlabel('Owner')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('deployments_by_owner.png', bbox_inches='tight')
plt.show()

# Plot 3: Count of Images by Environment
plt.figure(figsize=(10, 6))
df['environment'].value_counts().plot(kind='bar', color='coral')
plt.title('Count of Images by Environment')
plt.xlabel('Environment')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images_by_environment.png', bbox_inches='tight')
plt.show()

# Analysis: Max Age in Days
df['creation_timestamp'] = pd.to_datetime(df['creation_timestamp'], format='%Y-%m-%d %H:%M:%S')
df['age_in_days'] = (pd.to_datetime('today') - df['creation_timestamp']).dt.days

# Group by owner, namespace, and image_name
max_age_df = df.groupby(['owner', 'namespace', 'image_name'])['age_in_days'].max().reset_index()

# Add a column to indicate whether to replace or maintain
max_age_df['action'] = max_age_df['age_in_days'].apply(lambda x: 'replace' if x > 90 else 'maintain')

# Save max age analysis DataFrame as a CSV file
max_age_df.to_csv('max_age_analysis.csv', index=False)

# Detailed analysis grouped by namespace, owner, group, environment, and image_name
detailed_analysis = df.groupby(['namespace', 'owner', 'group', 'environment', 'image_name']).size().reset_index(name='count')
detailed_analysis.to_csv('detailed_analysis.csv', index=False)

# Additional grouping analysis
# Group by namespace and owner
namespace_owner_group = df.groupby(['namespace', 'owner']).size().reset_index(name='count')
namespace_owner_group.to_csv('namespace_owner_analysis.csv', index=False)

# Group by environment and image_name, and add columns for owner, namespace, age_in_days, and image_version
environment_image_group = df.groupby(['environment', 'image_name', 'owner', 'namespace', 'age_in_days', 'image_version']).size().reset_index(name='count')
environment_image_group.to_csv('environment_image_analysis.csv', index=False)

# Save summary DataFrame as a CSV file
df.to_csv('summary_k8s_deployments.csv', index=False)

# Display the final DataFrame
print(df.to_string(index=False))
