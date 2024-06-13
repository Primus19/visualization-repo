import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Read CSV file into DataFrame
csv_file = 'your_file.csv'  # Replace with your actual file path
df = pd.read_csv(csv_file)

# Convert 'instance_create_time' to datetime
df['instance_create_time'] = pd.to_datetime(df['instance_create_time'], errors='coerce')

# Display basic information about the DataFrame
print(df.info())

# Plot 1: Count of instances by db_instance_class
plt.figure(figsize=(10, 6))
df['db_instance_class'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Count of Instances by DB Instance Class')
plt.xlabel('DB Instance Class')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Count of instances by engine
plt.figure(figsize=(10, 6))
df['engine'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Count of Instances by Engine')
plt.xlabel('Engine')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Instances creation over time
plt.figure(figsize=(10, 6))
df.set_index('instance_create_time').resample('M').size().plot(color='coral')
plt.title('Instances Creation Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Instances Created')
plt.tight_layout()
plt.show()

# Plot 4: Distribution of engine versions
plt.figure(figsize=(10, 6))
df['engine_version'].value_counts().plot(kind='bar', color='orange')
plt.title('Distribution of Engine Versions')
plt.xlabel('Engine Version')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Additional Summary Statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Save plots to files
df['db_instance_class'].value_counts().plot(kind='bar', color='skyblue').figure.savefig('instances_by_class.png')
df['engine'].value_counts().plot(kind='bar', color='lightgreen').figure.savefig('instances_by_engine.png')
df.set_index('instance_create_time').resample('M').size().plot(color='coral').figure.savefig('instances_over_time.png')
df['engine_version'].value_counts().plot(kind='bar', color='orange').figure.savefig('engine_versions.png')

