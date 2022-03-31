
 """Write a Python program to print a specified list
    after removing the 0th, 4th and 5th elements,
    Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'], Expected
    Output: ['Green', 'White', 'Black']
"""
""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def removedIndex(li , removeIndexes):
    # Create new list for resultant list
    newList = []
    for i in range(0,len(li)):
        if( i  not in removeIndexes):
            newList.append(li[i])
    return newList
li = input("Enter a list :").split(",")
removeIndexes = input("Enter indexes of element to remove : ").split(",")
removeIndexesNew = [int(i) for i in removeIndexes]
li = removedIndex(li,removeIndexesNew)
print(li)
