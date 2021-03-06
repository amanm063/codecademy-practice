"""HYPOTHESIS TESTING
A/B Testing at Nosh Mish Mosh
The Nosh Mish Mosh is a recipe and ingredient meal delivery service. They ship the raw materials and you get to cook them at your home! They’ve decided to hire a data analyst to help make product and interface decisions. Get started to help them figure out the amount of data they’ll need to make meaningful decisions.

Note that a solution.py file is loaded for you in the workspace, which contains solution code for this project. We highly recommend that you complete the project on your own without checking the solution, but feel free to take a look if you get stuck or want to check your answers when you’re done!"""


#sorry i don't have the source for the data as it was pre-loaded into the interpreter of codecademy

import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)
baseline_percent =( paying_visitor_count/total_visitor_count) *100
print(baseline_percent)

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
new_customers_needed = np.ceil(1240/average_payment)

percentage_point_increase = (new_customers_needed / total_visitor_count*100)

mde = (percentage_point_increase/baseline_percent)*100
print(mde)
