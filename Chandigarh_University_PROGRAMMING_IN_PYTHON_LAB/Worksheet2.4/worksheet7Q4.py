""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

"""Write a Python program to convert a tuple of string values to a tuple of integer values"""
def strToIntegerInTuple(tup):
    newList = [int(item) for item in tup]
    return tuple(newList)


collection = '1','2','3','4','5'
print("Tuple before operation : ")
print(collection)
collection = strToIntegerInTuple(collection)
print("Tuple after operation : ")
print(collection)
