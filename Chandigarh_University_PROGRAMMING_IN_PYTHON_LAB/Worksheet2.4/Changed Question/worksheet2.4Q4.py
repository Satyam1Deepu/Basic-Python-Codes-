""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

"""Write python program to find the size and sum of tuple elements."""

def sizeAndSumOfTuple(tup):
    size = len(tup)
    summ = sum(tup)
    return (size , summ)

# Base code :
# Packing :
tup = 10,9,8,7,6,5,4,3,2,1
# Unpacking :
sizeOfTuple , sumOfTuple = sizeAndSumOfTuple(tup)
print("\nSatyam Kumar Deepu : 20BCS9274\n")
print('Size of tuple :',sizeOfTuple)
print('Sum of tuple : ',sumOfTuple)
