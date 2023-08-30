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
#Inspect DataFrame content
##STEP2: DATA WRANGLING
print("Content of DataFrame: ")
print(df.info())
print(df.head())
print("")
df.drop_duplicates(inplace=True)
print("DataFrame update:", df)
#Missing value
missing_values = df.isnull().sum()
print("Missing Values:", missing_values)
df = pd.read_csv('po1_data.txt', sep=",", header=None, names=columns )
df = pd.DataFrame(df, columns=columns)
