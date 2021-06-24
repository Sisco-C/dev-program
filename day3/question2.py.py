import numpy as np
chosen_month = input("Enter the number of your month of choice, eg January is month number 1: ")
chosen_year = input("Enter your year of choice: ")
# beginning = (chosen_month,- chosen_year,)
nextmonth = int(chosen_month) + 1
# print("beginning")
the_count = np.busday_count('{}-{}'.format(chosen_year, chosen_month), '{}-{}'.format(chosen_year, nextmonth))
# print("The number of workdays in ", chosen_month , "of", chosen_year , "is:", the_count, )
print('Number of weekdays in {} {} is: {}'.format(chosen_month, chosen_year, the_count))