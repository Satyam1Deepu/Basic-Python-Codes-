
"""Write a Python program calculate the product, multiplying all the numbers of a given tuple."""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def productOfTuple(tup):
    product = 1
    for i in range(0,len(tup)):
        product *= tup[i]
    return product

collection = (12,76,18,43,63)

print(" Value after multiplying all the numbers of a given tuple : ",productOfTuple(collection))
