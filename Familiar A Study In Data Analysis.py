"""Welcome to Familiar, a startup in the new market of blood transfusion! You’ve joined the team because you appreciate the flexible hours and extremely intelligent team, but the overeager doorman welcoming you into the office is a nice way to start your workday (well, work-evening).

Familiar has fallen into some tough times lately, so you’re hoping to help them make some insights about their product and help move the needle (so to speak)."""

#if anyone finds the link to the dataset then please mention it to me i will
#update these files


# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

print(lifespans.head(10))
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == "vein"]
print(vein_pack_lifespans)
print(np.mean(vein_pack_lifespans))

tstat , pval = ttest_1samp(vein_pack_lifespans,73)
print(pval)

artery_pack_lifespans = lifespans.lifespan[lifespans.pack == "artery"]
print(artery_pack_lifespans)
print(np.mean(artery_pack_lifespans))

stat,p = ttest_ind(vein_pack_lifespans,artery_pack_lifespans)
print(p)

print(iron.head())
Xtab = pd.crosstab(iron.pack,iron.iron)
print(Xtab)

chi2, p_2,dof,exp = chi2_contingency(Xtab)
print(p_2)
