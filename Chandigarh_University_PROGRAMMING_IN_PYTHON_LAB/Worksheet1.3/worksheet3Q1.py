"""
Write a python program to calculate area of 10 different circles. Given the pie = 22/7 
and radius of the circles entered by user using Simple Function , Parameterized Function ,
Return Type with function and return type with parameterized Functions.
"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def areaOfCircle (radius):
    return (22/7)*(radius**2)

# Base Code for functional Calling :
i = 0
while(i < 10):
    print(" Enter radius for which you want an area of circle : ")
    printAreaOfCircleOfRadius = float(input())
    print(areaOfCircle(printAreaOfCircleOfRadius))
    i += 1
