""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def binarySearch(arr,element):
    si = 0
    ei = len(arr) - 1
    mid = (si + ei)//2
    while(si < ei):
        if(arr[mid] < element):
            si = mid
            mid = (si + ei)//2
        elif(arr[mid] > element):
            ei = mid
            mid = (si + ei) // 2
        else:
            return mid
    return -1


arr = [1,3,2,4,0,6,8]
number = int(input("Enter number to find index of it : "))
index = binarySearch(arr,number)
if( index != -1):
    print("Found at : ",index )
else:
    print("Not found :(")
