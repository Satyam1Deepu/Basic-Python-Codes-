"""
Write a Python class named Rectangle constructed by a length and width and a method
which will compute the area of a rectangle
"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

class Rectangle :
    # Overridding init function of Object class in Rectangle class :
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return (self.length)*(self.width)

len = float(input("Enter length  for rectangle : "))
wid = float(input("Enter width  for rectangle : "))
rectangle = Rectangle(len,wid)
print("Area of rectangle : ",rectangle.area())
