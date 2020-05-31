# Python Homework Q1: PyBank

import os
import csv

# Set variables
NoOfMonth = 0
TotalProfit = 0
TotalChn = 0
Change = 0
Max = 0
Min = 0
Profit = 0

# READ FILE AND PROCESS THE DATA
# set file path to extract data
csvpath = os.path.join('..','Resources','budget_data.csv')

#open the file to read
with open(csvpath, 'r') as csvfile:
    # CSV reader split strings with specified delimiter to create variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    csv_header = next(csvreader)

    # Read each row of data, and proccess the information
    for row in csvreader:
        if Profit != 0 :
            Change = int(row[1]) - Profit
            TotalChn = TotalChn + Change

        Profit = int(row[1])
        NoOfMonth += 1
        TotalProfit = TotalProfit + Profit
        if Change > Max:
            Max = Change
            MaxMonth = str(row[0])
        elif Change < Min:
            Min = Change
            MinMonth = str(row[0])

AvgChn = round((TotalChn/ (NoOfMonth-1)),2)

# CREATE REPORT TEXT FILE
# Specify the file to write to
output_path = os.path.join('..','Analysis','PyBank.txt')

# Open the txt file, and write report in it
with open(output_path, "w", newline = '') as txt_file:
    txt_file.write("Financial Analysis \n") 
    txt_file.write("---------------------------- \n") 
    txt_file.write(f"Total Months:  {NoOfMonth} \n")
    txt_file.write(f"Total:  ${TotalProfit} \n")
    txt_file.write(f"Average  Change: ${AvgChn} \n")
    txt_file.write(f"Greatest Increase in Profits: {MaxMonth} (${Max}) \n")
    txt_file.write(f"Greatest Decrease in Profits: {MinMonth} (${Min}) \n")

# PRINT REPORT
print("")
print("***  PYBANK  ***") 
print("---------------------------- ") 
print("Financial Analysis ") 
print("---------------------------- ") 
print(f"Total Months:  {NoOfMonth} ")
print(f"Total:  ${TotalProfit} ")
print(f"Average  Change: ${AvgChn} ")
print(f"Greatest Increase in Profits: {MaxMonth} (${Max}) ")
print(f"Greatest Decrease in Profits: {MinMonth} (${Min}) ")
print("---------------------------- ") 
print("")


# Comparison from assignment txt
"""
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
"""