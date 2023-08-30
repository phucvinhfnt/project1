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
PPD_group = df[df['PDindicator29'] == 1]
non_PPD_group = df[df['PDindicator29'] == 0]
##STEP_6 IDENTIFY THE MOST SIGNIFICANT FEATURES T-TEST 2 sided
significant_features = []
results = []
for column in df.columns[1:-2]: # Exclude 'Subject identifier' and 'PD indicator' columns
    t_stat, p_value = ttest_ind(PPD_group[column], non_PPD_group[column])
    # print("\n Computing t*:", column)
    # print("\t t-statistic (t*): %.2f" % t_stat)
    # print("\n Computing p-value:", column)
    # print("\t p-value: %.4f" % p_value)
    # print("\n Conclusion:")
    if p_value < 0.05:
        conclusion = f"We reject the null hypothesis in {column}" 
        #Justify the hypothesis ==>
        significant_features.append(column) 
        #if p_value < 0.05:  # Consider features with p-value less than 0.05 as significant
        #significant_features.append(column)
    else:
        conclusion = f"We no reject the null hypothesis in {column}" 
        #Justify the hypothesis
    result = {
        "Feature": column,
        "T-statistic": t_stat,
        "p_value": p_value,
        "Conclusion": conclusion
    }
    results.append(result)
    
results_df=pd.DataFrame(results)
# print("\nResults:")
# print(results_df)
# print("Significant Features:", significant_features)
##STEP_5 VISUALIZATION FOR CORRELATION
significant_data = df[significant_features]
correlation_matrix = significant_data.corr()
#correlation_matrix.T.to_csv('correlation_matrix.csv')
print("Correlation Matrix between Significant Features:")
print(correlation_matrix)
##STEP_7 GRAPH SHOWING BOXPLOT BETWEEN 16 VARIABLES
plt.figure(figsize=(12, 10))
for i, feature in enumerate(significant_features):
    plt.subplot((len(significant_features) // 4) + 1, 4, i + 1)
    plt.boxplot([PPD_group[feature], non_PPD_group[feature]], labels=["PPD", "Non-PPD"])
    #plt.xlabel("PD indicator")
    plt.ylabel(feature)
    plt.title(f"Boxplot")
plt.tight_layout()
plt.show()
##STEP_8 GRAPH SHOWING THE HEATMAP TO VISUALIZATION CORRELATION
#HEATMAP
sns.heatmap(correlation_matrix, mask=np.zeros_like(correlation_matrix), annot=False, cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, fmt='.2f')
plt.show()
#Create box plot for showing the distribution of data in each column between PD and Non-PD
