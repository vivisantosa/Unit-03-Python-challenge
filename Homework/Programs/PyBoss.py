# Python Homework Q3: PyBoss

import os
import csv
import USStates 
csvpath = os.path.join('..','Resources','employee_data.csv')

#create lists to store data
# title = Emp ID,First Name,Last Name,DOB,SSN,State

Emp_ID = []
F_Name = []
L_Name = []
ListOfDOB = []
ListOfSSN = []
State = []

#fill the list while reading the source file row by row
# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(csvpath, 'r') as csvfile:   
    # Read the header row first (skip this step if there is no header)
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:

        # Employee ID column
        Emp_ID.append(row[0])
        #print(Emp_ID)

       # Split Name into 2 column First Name and Last Name
        name_split = row[1].split(" ")
        F_Name.append(name_split[0])
        L_Name.append(name_split[1])

        # Convert DOB
        DOB = (row[2])
        NewDOB = str(DOB[8:]) + "/" + str(DOB[5:7]) + "/" + str(DOB[:4])
        ListOfDOB.append(NewDOB)

        # Convert SSN, itu one with xxx-xx-XXXX
        OriginalSSN = (row[3])
        NewSSN = "xxx-xx-" + str(OriginalSSN[7:])
        ListOfSSN.append(NewSSN)
        
        # Abbreviate State using mapping through imported Dictionary - USStates.py
        s = (row[4])
        AbbrSt = (USStates.states[s])
        State.append(AbbrSt)
  
# Zip lists together
ConvertedList = zip(Emp_ID, F_Name, L_Name, ListOfDOB, ListOfSSN, State)

# CREATE REPORT TEXT FILE
# Specify the file to write to
output_path = os.path.join('..','Analysis','PyBoss.txt')

# Open the txt file, and write report in it
with open(output_path, "w", newline = '') as txt_file:
    txt_file.write("Employee ID, First Name, Last Name, Date of Birth, Social Security No, State")
    for employee in ConvertedList :
        txt_file.write (f"{employee} \n")

# CREATE CSV FILE
ConvertedList1 = zip(Emp_ID, F_Name, L_Name, ListOfDOB, ListOfSSN, State)

# Set variable for output file
output_file = os.path.join('..','Analysis','PyBoss.csv')

#  Open the output file
with open(output_file, "w", newline = '') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Employee ID", "First Name", "Last Name", "Date of Birth",
                     "Social Security No", "State"])

    # Write in zipped rows
    writer.writerows(ConvertedList1)


#PRINT REPORT
print("")
print("***  PYBOSS  ***") 
print("---------------------------- ") 
print("JOB DONE")
print("")