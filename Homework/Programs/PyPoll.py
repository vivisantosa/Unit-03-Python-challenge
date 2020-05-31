# Python Homework Q2: PyPoll

import os
import csv

# READ FILE AND PROCESS THE DATA
# set file path to extract data
csvpath = os.path.join('..','Resources','election_data.csv')

#CREATE CANDIDATE LIST
ListOfCand = []
ListOfVotes = []
#open the file to read
with open(csvpath, 'r') as csvfile:
    # CSV reader split strings with specified delimiter to create variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header, Count the vote
    for row in csvreader:
        Cand = (row[2])
        if Cand not in ListOfCand :
            ListOfCand.append(row[2])
            ListOfVotes.append(0)
        else:
            pass

# COUNT VOTES
Votes = 0
#open the file to read
with open(csvpath, 'r') as csvfile:
    # CSV reader split strings with specified delimiter to create variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header, Count the vote
    for row in csvreader:
        Votes += 1
        for Candidate in ListOfCand:
            if Candidate == (row[2]): 
                CandNo = ListOfCand.index(Candidate)
                ListOfVotes[CandNo] += 1

# CREATE REPORT FILE
# Specify the file to write to
output_path = os.path.join('..','Analysis','PyPoll.txt')

# Open the txt file, and write report in it
# Also find who is the winner (with finding Max votes, assign Max=0 to begin)
Max = 0
with open(output_path, "w", newline = '') as txt_file:
    txt_file.write("Election Results \n") 
    txt_file.write("---------------------------- \n") 
    txt_file.write(f"Total Votes: {Votes} \n")
    txt_file.write("---------------------------- \n") 

    for i in range(len(ListOfCand)):
        cand_name = ListOfCand[i]
        votes_count = ListOfVotes[i]
        percentage = int(round((votes_count*100/ Votes),2))
        txt_file.write(f"{cand_name}: {percentage}.000% ({votes_count}) \n")
        if votes_count > Max:
            Max = votes_count
            Winner = cand_name
    
    txt_file.write("---------------------------- \n") 
    txt_file.write(f"Winner: {Winner} \n")
    txt_file.write("---------------------------- \n") 


#PRINT REPORT
print("")
print("***  PYPOLL  ***") 
print("---------------------------- ") 
print("Election Results")
print("----------------------------")
print(f"Total Votes: {Votes}")
print("----------------------------")

for i in range(len(ListOfCand)):
    cand_name = ListOfCand[i]
    votes_count = ListOfVotes[i]
    percentage = int(round((votes_count*100/ Votes),2))
    print(f"{cand_name}: {percentage}.000% ({votes_count})")

print("----------------------------")
print(f"Winner: {Winner}")
print("----------------------------")
print("")


# Comparison from assignment txt
"""
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
"""