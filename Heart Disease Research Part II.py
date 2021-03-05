"""In this project, you’ll investigate some data from a sample patients who were evaluated for
heart disease at the Cleveland Clinic Foundation. The data was downloaded from the UCI
Machine Learning Repository and then cleaned for analysis. The principal investigators
responsible for data collection were:

Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D."""


#THE LINK FOR THE DATASET IS BELOW
#https://archive.ics.uci.edu/ml/datasets/Heart+Disease

# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency
# load data
heart = pd.read_csv('heart_disease.csv')

print(heart.head())
sns.boxplot(heart.heart_disease,heart.thalach)
plt.show()

thalach_hd = heart.thalach[heart.heart_disease == "presence"]
thalach_no_hd = heart.thalach[heart.heart_disease == "absence"]

print(np.mean(thalach_hd) - np.mean(thalach_no_hd))
print(np.median(thalach_hd) - np.median(thalach_no_hd))

tstat , pval  = ttest_ind(thalach_hd,thalach_no_hd)
print(pval)
plt.clf()
sns.boxplot(y=heart.trestbps,x=heart.sex)

plt.show()
trestbps_male = heart.trestbps[heart.sex == "male"]
trestbps_female = heart.trestbps[heart.sex == "female"]
tstat2 , pval_2 = ttest_ind(trestbps_male,trestbps_female)
print(pval_2)

sns.boxplot()
plt.clf()

sns.boxplot(y=heart.thalach , x=heart.cp)
plt.show()

thalach_typical = heart.thalach[heart.cp == "typical angima"]

thalach_asympton = heart.thalach[heart.cp == "asymptomatic"]

thalach_nonangin = heart.thalach[heart.cp == "non-anginal pain"]

thalach_atypical = heart.thalach[heart.cp == "atypical angima"]

Fstat,p_val = f_oneway(thalach_typical,thalach_asympton,thalach_nonangin,thalach_atypical)

print(p_val)

results = pairwise_tukeyhsd(endog = heart.thalach, groups = heart.cp)
print(results)

Xtab = pd.crosstab(heart["cp"],heart["heart_disease"],margins = False)
print(Xtab)

chi2,p,dof,exp = chi2_contingency(Xtab)
print(p)

#THANKS
