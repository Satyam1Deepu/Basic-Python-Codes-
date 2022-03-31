"""
    Write a Python program to get a list, sorted in increasing order
    by the last element in each tuple from a given list of non-empty tuples
"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

# Sorting List of Tuples in Increasing order by last element
def bubbleSortInListOfTuple(li):
    listLen = len(li);
    for i in range(0, listLen):
        for j in range(0, listLen - i - 1):
             if(li[j][-1] > li[j + 1][-1]):
                #swap:
                li[j],li[j + 1] = li[j + 1],li[j]
    return li

# Base code for functional calling :
li = [(2, 75, 45, 96, 15), (1, 2, 4, 9, 8, 3, 7), (67, 81, 34, 97, 91), (12, 76, 18, 43, 63)]
print("\nSatyam Kumar Deepu : 20BCS9274")
print("Status of list before : ",li)
print("Status of list after : ",bubbleSortInListOfTuple(li))
