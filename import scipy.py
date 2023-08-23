import scipy.stats as st
import numpy as np
sample = np.array([248,37,146,19,66,236,164,30,13,144,242,20])

x_bar= st.tmean(sample)
s=st.tstd(sample)
# print(x_bar,s)
t_stats,p_val =st.ttest_1samp(sample,88,alternative='greater')
print("T-stats:",t_stats)
print("p-value: ",p_val)
if p_val<0.05:
    print("\t we reject the null hypothesis.")
else:
    print("\t we acept the null hypothesis.")