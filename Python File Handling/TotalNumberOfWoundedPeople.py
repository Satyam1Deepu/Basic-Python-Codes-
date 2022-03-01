""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""
import csv

with open("C:\\Users\\satya\\Downloads\\year2017.csv", "r") as file_obj:
    file_data = csv.reader(file_obj)
    file_list = list(file_data)
    # Wounded Index = 10
    totalWounded = []
    for row in file_list[1:]:
        val = row[10]
        if val != '':
            totalWounded.append(float(val))
    print(int(sum(totalWounded)))