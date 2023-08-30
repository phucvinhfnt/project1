import statistics as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st
import statsmodels.stats.weightstats as stm
import math
from sklearn import tree
from scipy.stats import ttest_ind
##STEP1: DATA PROCESSING 
#Creat a new table with labelled columns
columns = [
    "Subjectidentifier1", "Jitter2", "Jitter3", "Jitter4", "Jitter5", "Jitter6", "Shimmer7", 
    "Shimmer8", "Shimmer9", "Shimmer10", "Shimmer11", "Shimmer12", "Harmonicity13", 
    "Harmonicity14", "Harmonicity15", "Pitch16", "Pitch17", "Pitch18", "Pitch19", "Pitch20",
    "Pulse21", "Pulse22", "Pulse23", "Pulse24", "Voice25", "Voice26", "Voice27", "UPDRS28",
    "PDindicator29",
]
df = pd.read_csv('po1_data.txt', sep=",", header=None, names=columns )
df = pd.DataFrame(df, columns=columns)
##STEP3: DESCRIPTIVE STATISTICS
print(df)
df.T.to_csv('df.csv')
print(df.describe())
df.describe().T.to_csv('descriptive statistics.csv') 
##STEP_4 VISUALIZATION HISTOGRAM FOR 26 VARIABLES
# Graph showing mean by PD and Non-PD
columns = df.columns[1:-1]  # Not included columns "Subject Identifier" and PD
num_columns = len(columns)
plt.figure(figsize=(12, 10))
for i in range(num_columns-1):
    plt.subplot((num_columns // 4) + 1, 4, i + 1)
    # plt.figure(figsize=(6, 8))
    plt.hist(df[columns[i]], bins=10, color='blue', alpha=0.7)
    # plt.xlabel(columns[i])
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {columns[i]}')
plt.tight_layout()
plt.show()
##STEP_5 PERFORM A STATISTICAL ANALYSIS BETWEEN TWO GROUP
PPD_group = df[df['PDindicator29'] == 1]
non_PPD_group = df[df['PDindicator29'] == 0]
# Graph showing mean by PD and Non-PD
columns = df.columns[1:-2]  # Not included columns "Subject Identifier" and PD
num_columns = len(columns)
# # Graph showing mean by PD and Non-PD
# columns = df.columns[1:-1]  # Not included columns "Subject Identifier" and PD
# num_columns = len(columns)
plt.figure(figsize=(12, 10))
for i in range(num_columns-1):
    plt.subplot((num_columns // 4) + 1, 4, i + 1)  # Set row and column of subplots
    plt.bar(["PD", "Non-PD"], [PPD_group[columns[i]].mean(), non_PPD_group[columns[i]].mean()])
    #plt.xlabel("Group")
    #plt.ylabel("Mean " + columns[i])
    plt.title("Mean " + columns[i])
plt.tight_layout()
plt.show()

