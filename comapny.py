#it is a project on startup transformation that is learned through codecademy
# sorry i don't have all the necessary csv files as they were not provided to me
#but if any of you is working on it then it is how to do this as well as other stelps towards making a new project
# i am uploading it cause it is one of the very  first project that i have upon by myself.

import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
print(financial_data.head(20))
month = financial_data["Month"]
revenue = financial_data["Revenue"]
expenses = financial_data["Expenses"]
plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()

plt.clf()
plt.plot(month,expenses)
plt.xlabel("Month")
plt.ylabel("Amount($)")
plt.title("Expenses")
plt.show()

expenses_overview = pd.read_csv("expenses.csv")
print(expenses_overview.head(7))

expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]

plt.clf()
plt.pie(proportions , labels = expense_categories)
plt.axis('Equal')
plt.tight_layout()
plt.show()

expense_cut = "office rent"

employees = pd.read_csv("employees.csv")
print(employees.head())

sorted_productivity = employees.sort_values(by = ["Productivity"] )
print(sorted_productivity)

employees_cut = sorted_productivity.head(100)
print(employees_cut)

transformation = "standardization"

commute_times = employees["Commute Time"]
print(commute_times.describe())
commute_times_log = np.log(commute_times)

plt.clf()
plt.hist(commute_times_log)
plt.title("commute times")
plt.xlabel("employee")
plt.ylabel("time")
plt.show()


#thank you
