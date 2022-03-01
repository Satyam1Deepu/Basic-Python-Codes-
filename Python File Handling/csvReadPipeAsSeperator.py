""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

import csv
with open("C:\\Users\\satya\\Downloads\\year2017.csv","r") as file_obj :
    file_data = csv.reader(file_obj)
    # Iterate over that list ( It was W/O indexing)
    file_list = list(file_data)
    print()
    for row in file_list:
        print(row)
 
print(type(file_data))