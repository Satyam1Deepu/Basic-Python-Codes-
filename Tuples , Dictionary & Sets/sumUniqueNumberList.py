""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def sumUnique(numList):
    # Created empty set :
    # sets = {} ----> Dictionary not a set
    sets = set()
    for element in  numList :
        sets.add(element)
    # Only unique values will be present in our set :
    # create sum variable to store sum , iterate over set & add each values in sum
    sum = 0
    for element in sets :
        sum += element
    return sum

# Base Code for functional programming :
# n(n+1)//2 = 55
print(sumUnique([1,2,3,4,5,6,7,8,9,10]))
