"""Brian is a Product Manager at FarmBurg, a company that makes a farming simulation social network game. In the FarmBurg game, you can plow, plant, and harvest different crops. ​Brian has been conducting an A/B Test with three different variants, and he wants you to help him analyze the results. Using the Python modules pandas and SciPy, you will help him make some important business decisions!"""
# Import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import binom_test

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')
print(abdata.head())
xtab = pd.crosstab(abdata.group,abdata.is_purchase)
print(xtab)
chi2 , p , dof,exp = chi2_contingency(xtab)
print(p)
num_visits = len(abdata)
print(num_visits)

num_sales_needed_099 = 1000/0.99
print(round(num_sales_needed_099))
p_sales_needed_099 = num_sales_needed_099/num_visits 
print(p_sales_needed_099)

num_sales_needed_199 = 1000/1.99
print(round(num_sales_needed_199))
p_sales_needed_199 = num_sales_needed_199/num_visits 
print(p_sales_needed_199)

num_sales_needed_499 = 1000/4.99
print(round(num_sales_needed_499))
p_sales_needed_499 = num_sales_needed_499/num_visits
print(p_sales_needed_499)

samp_size_099 = np.sum(abdata.group == "A")
print(samp_size_099)

sales_099 = np.sum((abdata.group =="A") & (abdata.is_purchase == "Yes")) 
print(sales_099)

samp_size_199 = np.sum(abdata.group == "B")
print(samp_size_199)

sales_199 = np.sum((abdata.group =="B") & (abdata.is_purchase == "Yes")) 
print(sales_199)

samp_size_499 = np.sum(abdata.group == "C")
print(samp_size_499)

sales_499 = np.sum((abdata.group =="C") & (abdata.is_purchase == "Yes")) 
print(sales_499)

pvalueA = binom_test(x=sales_099,n=samp_size_099,p=0.20,alternative="greater")
print(pvalueA)


pvalueB = binom_test(x=sales_199,n=samp_size_199,p=0.10,alternative="greater")
print(pvalueB)


pvalueC = binom_test(x=sales_499,n=samp_size_499,p=0.04,alternative="greater")
print(pvalueC)
