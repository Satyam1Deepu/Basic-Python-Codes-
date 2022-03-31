""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

""" Write a Python program to remove an empty tuple(s) from a list of tuples."""

li = [(2,75,45,96,15),(),(1,2,4,9,8,3,7),(67,81,34,97,91),(),(12,76,18,43,63)]
print(" List of tuples before :")
print(li)
i = 0
while(i < len(li)):
    if(len(li[i]) == 0):
        del li[i]
    i += 1
print(" List of tuples after :")
print(li)
