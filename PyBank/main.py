# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# *The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# *(Thankfully, your company has rather lax standards for accounting so the records are simple.)
# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The total net amount of "Profit/Losses" over the entire period

#   * The average change in "Profit/Losses" between months over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal 
# * and export a text file with the results.

# ******************************************************************************

# First import the os module
# create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')

# with open(csvpath, 'r') as file_handler:
#         PyBank = file_handler.read()
# print(PyBank)
# # print(type(PyBank))

######################################################

# #   The total number of months included in the dataset
total_months = 0
with open(csvpath) as csvfile:
    PyBank = csv.DictReader(csvfile)
#    PyBank = {"Date": "Jan-2010", "Profit/Losses": 867884}
    for row in PyBank:
        total_months = total_months + 1
    print("The total months is " + str(total_months))
#    print(Pybank.keys)

##############################################################
#   The total net amount of "Profit/Losses" over the entire period

#total_P_L = 0
#   PyBank = {"Date": "Jan-2010", "Profit/Losses": 867884}
#    print(Pybank.keys)
    for Profit/Losses in PyBank():
        total_P_L = sum(int(Profit/Losses) + int(total_P_L))
#     print(f''total_P_L)

##############
#   The average change in "Profit/Losses" between months over the entire period
# avareage_change = 0
# con_months = []
# for x in range
#     for change in Profit/Losses:

# #   The greatest increase in profits (date and amount) over the entire period
# Max_inc = 0
# if 
# #   The greatest decrease in losses (date and amount) over the entire period
# Max_dec = 0

# #   ```format the data
print("FIinancial Analysis")
print('----------------------------')
# #   Total Months: 86
#    print("The total months is " + str(total_months))
# #   Total: $38382578
# #   Average  Change: $-2315.12
# #   Greatest Increase in Profits: Feb-2012 ($1926159)
# #   Greatest Decrease in Profits: Sep-2013 ($-2196167)
# #   ```


