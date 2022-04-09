""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

"""Implement Unpacking of tuples in multiple variables."""

def sumAndMultiplyOfTuple(tup):
    summ = sum(tup)
    mul = 1
    for item in tup:
        mul *= item
    return (summ , mul)

# Packing of tuple :
tup = (1,2,3,4,5,6,7,8,9,10)
print("\nSatyam Kumar Deepu : 20BCS9274\n")
# Unpacking of tuple :
summation , multiplication  = sumAndMultiplyOfTuple(tup)
print("Sum of tuple : ",summation)
print("Multiplication of tuple : ",multiplication)
