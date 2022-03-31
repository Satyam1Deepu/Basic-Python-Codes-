""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

"""Write a Python program to check if a specified element presents in a tuple of tuples"""
def isFound(tup,element):
    found = False
    for i in range(0,len(collection)):
        for j in range(0,len(collection[i])):
            if(element == collection[i][j]):
               found = True
               return found


collection = ((2,75,45,96,15),(1,2,4,9,8,3,7),(67,81,34,97,91),(12,76,18,43,63))

number = int(input("Enter number to remove from tuple of tuples :"))

if(isFound(collection,number)):
    print("Number found !!! ")
else:
    print("Number not found :(")
