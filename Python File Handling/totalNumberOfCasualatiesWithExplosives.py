""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

import csv

with open("C:\\Users\\satya\\Downloads\\year2017.csv", "r") as file_obj:
    file_data = csv.reader(file_obj)
    file_list = list(file_data)
    # Weapon_typeIndex = 14
    # Casualities Index = 15
    totalCasualities = []
    for row in file_list[1:]:
        val = row[15]

        if (val != '' and row[14] =="Explosives"):
            totalCasualities.append(float(val))
    print(int(sum(totalCasualities)))
