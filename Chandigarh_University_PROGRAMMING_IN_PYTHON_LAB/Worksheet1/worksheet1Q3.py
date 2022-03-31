"""
Write a  program to enter length in centimeter and convert it into
meter and kilometer,and also convert the same into Equivalents 
"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

print("Enter Length (Unit : cm ) : ")
length = float(input())
# Converting :
print("In meters : ", (length / 100))
print("In Kilometers : ", (length / 1000000))

print("Enter Length (Unit : m ) : ")
length = float(input())
# Converting :
print("In centimeter: ", (length*100))
print("In Kilometers : ", (length / 1000))

print("Enter Length (Unit : Km ) : ")
length = float(input())
# Converting :
print("In Centimeters : ", (length*1000000))
print("In meters : ", (length*1000))
