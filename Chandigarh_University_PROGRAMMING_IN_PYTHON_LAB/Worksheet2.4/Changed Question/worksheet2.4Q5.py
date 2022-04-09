""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

# List of tuple's first value is for sorting  : Modified bubbleSort
def sortListOfTupleByFirstItem(arr):
        length = len(arr)
        for i in range(length - 1):
            for j in range(length - 1 - i):
                if (arr[j][0] > arr[j + 1][0]):
                    # swap
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

# Base code for functional calling :
li = [(2, 75, 45, 96, 15), (1, 2, 4, 9, 8, 3, 7), (67, 81, 34, 97, 91), (12, 76, 18, 43, 63)]
print("\nSatyam Kumar Deepu : 20BCS9274\n")
print("List of tuple before sorting :")
print(li)
print()
li = sortListOfTupleByFirstItem(li)
print("List of tuple after sorting :")
print(li)
