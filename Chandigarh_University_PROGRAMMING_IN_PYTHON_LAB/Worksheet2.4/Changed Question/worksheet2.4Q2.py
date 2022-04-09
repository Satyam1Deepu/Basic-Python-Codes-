""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

"""Write a Python program to find the repeated items of a tuple"""
# defined tuple :
tup = (1,5,1,8,6,4,6,4,6,45,5,2,4,47,8,25,5)
print("\nSatyam Kumar Deepu : 20BCS9274\n")
print('Displaying tuple : ',tup,"\n")
#defined empty dictionary for storing frequency of numbers :
dic = {}
for item in tup:
    dic[item] = dic.get(item,0) + 1

print("Displaying items repeated in tuple :")
for item in dic.keys():
    # number having frequency more than 1 will get printed :
    if(dic[item] > 1):
        print(item)
