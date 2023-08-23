
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind  # Import ttest_ind from scipy.stats 

# Specify the file path
file_path = "po1_data.txt"  # Replace with the actual file path

# Initialize an empty list to store the data
data = []

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read each line in the file
    for line in file:
        # Split the line into individual values (assuming comma-separated values)
        values = line.strip().split(',')
        # Convert each value to the appropriate data type (e.g., float)
        values = [float(val) for val in values]
        # Append the values to the data list
        data.append(values)

# Column names for the dataset
columns = [
    'Subject identifier', 'Jitter (%)', 'Jitter (abs)', 'Jitter (rap)', 'Jitter (ppq5)', 'Jitter (ddp)',
    'Shimmer (%)', 'Shimmer (abs)', 'Shimmer (apq3)', 'Shimmer (apq5)', 'Shimmer (apq11)', 'Shimmer (dda)',
    'Harmonicity (ac)', 'Harmonicity (NHR)', 'Harmonicity (HNR)', 'Pitch (median)', 'Pitch (mean)',
    'Pitch (std)', 'Pitch (min)', 'Pitch (max)', 'Pulse (num)', 'Pulse (periods)', 'Pulse (mean period)',
    'Pulse (std period)', 'Voice (unvoiced frames)', 'Voice (num voice breaks)', 'Voice (degree voice breaks)',
    'UPDRS', 'PD indicator'
]

# Create a DataFrame from the data and column names
df = pd.DataFrame(data, columns=columns)

# Print the DataFrame to verify the results
#print(df)


# Step 3: Explore the dataset
print(df.head())  # Display the first few rows of the dataset
print(df.describe())  # Summary statistics of the dataset

# Step 4: Perform a statistical analysis
PPD_group = df[df['PD indicator'] == 1]
non_PPD_group = df[df['PD indicator'] == 0]

# Step 5: Identify the most significant features
significant_features = []
for column in df.columns[1:-2]:  # Exclude 'Subject identifier' and 'PD indicator' columns
    t_stat, p_value = ttest_ind(PPD_group[column], non_PPD_group[column])
    if p_value < 0.05:  # Consider features with p-value less than 0.05 as significant
        significant_features.append(column)

print("Significant Features:", significant_features)

# Step 6: Visualize the important features
for feature in significant_features:
    plt.figure(figsize=(8, 6))
    plt.boxplot([PPD_group[feature], non_PPD_group[feature]], labels=["PPD", "Non-PPD"])
    plt.xlabel("PD indicator")
    plt.ylabel(feature)
    plt.title(f"Boxplot of {feature} between PPD and Non-PPD groups")
    plt.show()