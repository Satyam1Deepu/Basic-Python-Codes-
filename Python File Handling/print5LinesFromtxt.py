""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

file_obj = open("C:\\Users\\satya\\Downloads\\Sample.txt","r")

file_data = file_obj.readlines()
print("Total number of lines : ",len(file_data))
i = 0
while ( i < 5):
   print(file_data[i])
   i += 1