import scipy.stats as st
import numpy as np 
#group that volunteers
x_bar1=105.32
s1=14.68
n1=57
#group that does not volunteer
x_bar2=96.82
s2=14.26
n2=17
t_stats,p_val = st.ttest_ind_from_stats(x_bar1,s1,n1,x_bar2,s2,n2,equal_var=False,alternative='two-sided')
print("t-sats" ,t_stats)
print("pvalue:", p_val)
if p_val<0.05:
    print("\t we reject the null hypothesis.")
else:
    print("\t we acept the null hypothesis.")