""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

# Opening .txt file :

file_obj = open("C:\\Users\\satya\\Downloads\\Sample.txt","r")
# To read only 100 bytes
#file_data = file_obj.read(100)
#print(type(file_data))
#print(file_data)
# To read only line :
file_data = file_obj.readline()
print(file_data)