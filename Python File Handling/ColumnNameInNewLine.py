""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

import csv
with open("C:\\Users\\satya\\Downloads\\year2017.csv", "r") as file_obj :
    file_data = csv.reader(file_obj)
    # Coverted Data into list :
    file_list = list(file_data)
    # Outer loop for accessing 1st Row i.e : Column Names
    for row in file_list[:1]:
        # Inner loop for iterating over columns & print on new line
        i = 0
        # Written 15 for printing columns from [0,15] i.e 16 columns
        while(i <= 15):
         print(row[i])
         i += 1
