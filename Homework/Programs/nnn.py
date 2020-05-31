# Python Homework Q4: PyParagraph

import os
import csv
import re

# READ FILE AND PROCESS THE DATA
# set file path to extract data
csvpath = os.path.join('..','Resources','paragraph_0.txt')

#open the file to read and extract text to analyse
with open(csvpath, 'r') as file_handler:
    text = file_handler.read()

# count the number of characters
NoOfLetters = len(text) - text.count(' ')

# splits at space to find words
w = text.split()
NoOfWords = len(w)
#print(w)

# splits at dot (.) to find sentences
s = re.split("(?<=[.!?]) +", text)
NoOfSnts = len(s)

AverageL = round((NoOfLetters/NoOfWords),1)
AverageS = round((NoOfWords/NoOfSnts),1)

# CREATE REPORT FILE
# Specify the file to write to
output_path = os.path.join('..','Analysis','PyParagraph.txt')

# Open the txt file, and write report in it
with open(output_path, "w", newline = '') as txt_file:
    txt_file.write("Paragraph Analysis \n") 
    txt_file.write("---------------------------- \n") 
    txt_file.write(f"Approximate Word Count: {NoOfWords} \n")
    txt_file.write(f"Approximate Sentence Count: {NoOfSnts} \n")
    txt_file.write(f"Average Letter Count: {AverageL} \n")
    txt_file.write(f"Average Sentence Length: {AverageS} \n")


#PRINT REPORT
print("")
print("***  PY PARAGRAPH  ***") 
print("---------------------------- ") 
print("Paragraph Analysis")
print("----------------------------")
print(f"Approximate Word Count: {NoOfWords}")
print(f"Approximate Sentence Count: {NoOfSnts}")
print(f"Average Letter Count: {AverageL}")
print(f"Average Sentence Length: {AverageS}")
print("----------------------------")