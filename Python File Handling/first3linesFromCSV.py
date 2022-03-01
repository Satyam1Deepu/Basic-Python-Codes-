""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

import csv

file_obj = open("C:\\Users\\satya\\Downloads\\year2017.csv","r")
file_data = csv.reader(file_obj)

print(type((file_data)))
# _csv.reader object doesn't support indexing :
# for indexing do typecasting in list Or Use for Loop :
"""This will Not Work 
i = 0
while ( i < 3 ):
    print(file_data[i])
    i += 1
"""
for row in file_data:
    print(row)
