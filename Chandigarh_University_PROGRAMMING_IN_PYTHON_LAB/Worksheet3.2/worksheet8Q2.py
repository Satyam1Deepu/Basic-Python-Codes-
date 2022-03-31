""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def bubbleSort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if(arr[j] > arr[j+1]):
                # swap
                arr[j],arr[j+1] = arr[j+1],arr[j]
  
arr = [6,5,4,3,2,1]

bubbleSort(arr)
print(arr)
