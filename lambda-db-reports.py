import pandas as pd
import matplotlib.pyplot as plt
import json

# Read CSV file into DataFrame
csv_file = 'FedRAMP-RDS-Upgrades - Uber Sheet.csv'  # Replace with your actual file path
df = pd.read_csv(csv_file)

# Sum of Instance Names by ENV
env_summary = df.groupby('Env')['Instance Name'].count().reset_index()
env_summary.columns = ['Env', 'Instance Count']

# Number of instances with tickets by ENV
df['Has Ticket'] = df['Ticket'].apply(lambda x: 1 if pd.notna(x) and x != "these were deleted in commercial" else 0)
tickets_summary = df.groupby('Env')['Has Ticket'].sum().reset_index()
tickets_summary.columns = ['Env', 'Ticket Count']

# Number of instances marked as deleted by ENV
df['Is Deleted'] = df['Ticket'].apply(lambda x: 1 if x == "these were deleted in commercial" else 0)
deleted_summary = df.groupby('Env')['Is Deleted'].sum().reset_index()
deleted_summary.columns = ['Env', 'Deleted Count']

# Merge summaries
summary = env_summary.merge(tickets_summary, on='Env').merge(deleted_summary, on='Env')

# Add a column for Completed Status
summary['Completed Status'] = ''

# Save the summary as a CSV file
summary.to_csv('rds_upgrades_summary.csv', index=False)

# Report 1: Summary of Instance Names by ENV
env_summary.to_csv('rds_upgrades_env_summary.csv', index=False)

# Report 2: Number of Instances with Tickets by ENV
tickets_summary.to_csv('rds_upgrades_tickets_summary.csv', index=False)

# Report 3: Number of Instances Marked as Deleted by ENV
deleted_summary.to_csv('rds_upgrades_deleted_summary.csv', index=False)

# Display DataFrames in nicely formatted tables using pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

# Print the nicely formatted DataFrames
print("\nSummary DataFrame:")
print(summary.to_string(index=False))

print("\nENV Summary:")
print(env_summary.to_string(index=False))

print("\nTickets Summary:")
print(tickets_summary.to_string(index=False))

print("\nDeleted Summary:")
print(deleted_summary.to_string(index=False))
