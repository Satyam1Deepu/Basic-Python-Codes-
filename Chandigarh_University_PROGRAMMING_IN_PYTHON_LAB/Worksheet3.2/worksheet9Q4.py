"""    
Write a Python class named Circle constructed by a radius and two methods
which will compute the area and the perimeter of a circle
"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

class Circle:
    pi = 3.14159
    def __init__(self,radius):
        self.radius = radius
    # Instance method :
    def area(self):
       return (Circle.pi)*(self.radius**2)
    def perimeter(self):
        return 2*(Circle.pi)*(self.radius)

rad = float(input("Enter radius of circle : "))
circle = Circle(rad)
print("Area of circle : ",circle.area())
print("Perimeter of circle : ",circle.perimeter())
