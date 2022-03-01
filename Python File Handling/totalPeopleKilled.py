""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

import csv

with open("C:\\Users\\satya\\Downloads\\year2017.csv", "r") as file_obj:
    file_data = csv.reader(file_obj)
    # Iterate over that list ( It was W/O indexing)
    file_list = list(file_data)

killed = []
# Slicing List with removing header ( Column names from CSV file :
for row in file_list[1:]:
    # 9th column is for number of person killed :
    # Missing Values : Skip those values i.e : ''
    val = row[9]
    if val != '':
      killed.append(float(val))

print(int(sum(killed)))
