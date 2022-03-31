"""
Write a python program to print Multiplication tables from 2 to 20 whether table values entered by user using 
Simple Function , Parameterized Function , Return Type with function and return type with parameterized Functions .
"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def printTable(tableof):
    i = 1
    while( i <= 10):
        print(tableof ," x ", i," = ",tableof*i)
        i += 1

print(" Enter number from which you want to print Table : ")
printTableFrom = int(input())
print(" Enter number upto which you want to print Table : ")
printTableUpto = int(input())

# Base Code for functional Calling :
while( printTableFrom <= printTableUpto):
    printTable(printTableFrom)
    print()
    printTableFrom += 1
