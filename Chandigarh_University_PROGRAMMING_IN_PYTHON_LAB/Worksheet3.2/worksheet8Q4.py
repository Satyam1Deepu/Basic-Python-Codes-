""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def selectionSort(arr):
    length = len(arr)
    for i in range(length - 1):
        minIndex = i
        # Calculating the index of minimum element for this iteraton
        for j in range(i+1,length):
            if(arr[j] < arr[minIndex]):
                minIndex = j
        #swap
        arr[i],arr[minIndex] = arr[minIndex],arr[i]

arr = [1,3,2,4,0,6,8]
selectionSort(arr)
print(arr)
