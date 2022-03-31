""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def linearSearch ( li ,element ):
    for i in range(len(li)):
        if(li[i]==element):
            return i
    return -1


# Base Code for Functional Calling :
li = [1,2,3,5,8,9]
print("Enter element to search index of element in a List : ")
elementToSearch = int(input())
index = linearSearch(li,elementToSearch)
print(index ," is the  index of Element ")
