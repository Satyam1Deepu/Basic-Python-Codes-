""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def bubbleSortByValueOfEachTuple(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if(arr[j][-1] > arr[j+1][-1]):
                # swap
                arr[j][-1],arr[j+1][-1] = arr[j+1][-1],arr[j][-1]
    return arr

d1 = {'a': 100, 'b': 200, 'c':300 , "d": 357 , "e":458}
# Empty List :
List = []
# Converted dictionary to list of pair of tuple :
for i in d1:
    List.append((i,d1[i]))
# Sorted List item on the basis of Value :
sortedList = bubbleSortByValueOfEachTuple(List)
# Printed 3 Highest value with corresponding keys :
for i in range(-3,0):
    print( sortedList[i][-2], " : ",sortedList[i][-1])
