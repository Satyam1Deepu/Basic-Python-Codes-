"""Write a Python program to replace last value of tuples in a list"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

# Removes element from tuple : We need to pass tuple & Index of element to be removed
def remove(tup,tupleIndex):
    newList = []
    for i in range(0,len(tup)):
        if(i == tupleIndex):
            continue
        newList.append(tup[i])
    return tuple(newList)
# Tuple :
collection = 1,2,3,4,8,7,9,19,12
# Calling function 
collection = remove(collection, len(collection ) -1)
print(collection)
