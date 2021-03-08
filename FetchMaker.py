"""Congratulations! You’ve just started working at the hottest new tech startup, FetchMaker. FetchMaker’s mission is to match up prospective dog owners with their perfect pet. FetchMaker has been collecting data on their adoptable dogs, and it’s your job to analyze some of that data."""
# Import libraries
import numpy as np
import pandas as pd
import codecademylib3
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency
# Import data
dogs = pd.read_csv('dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

print(dogs.head())

whippet_rescue = dogs.is_rescue[dogs.breed == "whippet"]
print(whippet_rescue.head())

num_whippet_rescues = np.sum(whippet_rescue == 1)
print(num_whippet_rescues)
num_whippets = len(whippet_rescue)
print(num_whippets)


pval = binom_test(x=num_whippet_rescues,n=num_whippets,p=0.08)

print(pval)

wt_whippets = dogs.weight[dogs.breed == "whippet"]
wt_terriers = dogs.weight[dogs.breed == "terrier"]
wt_pitbulls = dogs.weight[dogs.breed == "pitbull"]

stat,p = f_oneway(wt_whippets,wt_terriers,wt_pitbulls)
print(p)

results = pairwise_tukeyhsd(endog=dogs_wtp.weight,groups = dogs_wtp.breed)
print(results)
print(dogs_ps.head())
xtab = pd.crosstab(dogs_ps.breed,dogs_ps.color)
print(xtab)

chi2,p2,dof,exp = chi2_contingency(xtab)
print(p2)
