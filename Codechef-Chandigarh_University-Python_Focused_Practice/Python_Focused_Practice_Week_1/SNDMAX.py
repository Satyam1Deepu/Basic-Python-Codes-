""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""
"""
Problem Statement
Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.

Sample Input
3
1 2 3
10 15 5
100 999 500

Sample Output
2
10
500

Time Complexity : O(N^2)
Space Complexity : O(N)
"""
def bubbleSort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if(arr[j] > arr[j+1]):
                # swap
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

testcase = int(input())
for i in range(0,testcase):
    li = input().split( )
    newList = [int(i) for i in li]
    newListSorted = bubbleSort(newList)
    print(newListSorted[len(newListSorted)- 2 ])
