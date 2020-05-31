# Python Homework Q4: PyParagraph

import os
import csv
import re

Titles = ["Letters Count","Word Count","Sentence Count","Average Letter Count","Average Sentence Count"]

# READ FILE AND PROCESS THE DATA
# "my_file_converter" - is my function definition that 
# takes and opens file that located in the path describe in ("file_path"), and
# evaluate the text and report the answer as a list called Answers

def my_file_converter(file_path):
    #open the file to read and extract text to analyse
    with open(file_path, 'r') as file_handler:
        text = file_handler.read()

        Answers = []
        # count the number of characters
        NoOfLetters = len(text) - text.count(' ')
        Answers.append(NoOfLetters)

        # splits at space to find words
        w = text.split()
        NoOfWords = len(w)
        Answers.append(len(w))

        # splits at dot (.) to find sentences
        s = re.split("(?<=[.!?]) +", text)
        NoOfSnts = len(s)
        Answers.append(len(s))

        AverageL = round((NoOfLetters/NoOfWords),1)
        Answers.append(AverageL)
        AverageS = round((NoOfWords/NoOfSnts),1)
        Answers.append(AverageS)

        return Answers

# CREATE REPORT FILE
# This definition open the txt file, and write the report from the list ()
# "my_file_converter" - is my function definition that 
# creates a txt file in the path describe in ("output_path"), and
# writes report from a list that is processed from previous function definition (called Answers)

def my_file_maker(output_path, my_output):
    with open(output_path, "w", newline = '') as txt_file:
        txt_file.write("Paragraph Analysis \n") 
        txt_file.write("---------------------------- \n") 

        for i in range(1,5):
            txt_file.write(f"{Titles[i]}: {my_output[i]} \n")


# set file paths to extract data
csvpath = os.path.join('..','Resources','paragraph_0.txt')
csvpath1 = os.path.join('..','Resources','paragraph_1.txt')
csvpath2 = os.path.join('..','Resources','paragraph_2.txt')

#This portion runs the my_file_reader function aon all my three csvs
Answer = my_file_converter(csvpath)
Answer1 = my_file_converter(csvpath1)
Answer2 = my_file_converter(csvpath2)

# Specify the files to write to
output_path = os.path.join('..','Analysis','PyParagraph.txt')
output_path1 = os.path.join('..','Analysis','PyParagraph1.txt')
output_path2 = os.path.join('..','Analysis','PyParagraph2.txt')

#This portion runs the my_file_maker function on my output from the file reader function
my_file_maker(output_path, Answer)
my_file_maker(output_path1, Answer1)
my_file_maker(output_path2, Answer2)

#PRINT REPORT
print("")
print("***  PY PARAGRAPH  ***") 
print("---------------------------- ") 
print("Paragraph Analysis")
print("-----------------")

print("Answer for paragraph_0.txt are")
for i in range(1,5):
    print(f"{Titles[i]}: {Answer[i]}")
print("----------------------------")

print("Answer for paragraph_1.txt are")
for i in range(1,5):
    print(f"{Titles[i]}: {Answer1[i]}")
print("----------------------------")

print("Answer for paragraph_2.txt are")
for i in range(1,5):
    print(f"{Titles[i]}: {Answer2[i]}")
print("----------------------------")

