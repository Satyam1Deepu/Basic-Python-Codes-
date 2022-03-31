""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def binarySearch(arr,element):
    si = 0
    ei = len(arr) - 1
    mid = (si + ei)//2
    while(si < ei):
        if(arr[mid] == element):
            return mid
        elif(arr[mid] < element):
            si = mid + 1
        elif(arr[mid] > element):
            ei = mid - 1
    return -1


arr = [1,3,2,4,0,6,8]
number = int(input("Enter number to find index of it : "))
index = binarySearch(arr,number)
if( index != -1):
    print("Found at : ",index )
else:
    print("Not found :(")
