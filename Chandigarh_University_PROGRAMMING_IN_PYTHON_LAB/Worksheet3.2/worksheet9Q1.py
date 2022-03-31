"""    
Write a Python class named Student with two attributes student_id, student_name. 
Add a new attribute student_class and display the entire attribute and their values of the said class.
Now remove the student_name attribute and display the entire attribute with values
"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

class Student:
    # Overridding init function of Object class in Student class :
    def __init__(self,student_id , student_name):
      self.student_id = student_id
      self.student_name = student_name


student1 = Student("20BCS9274" ,"Satyam Kumar Deepu")
# Adding a new attribute student_class : 
student1.student_class = 'Btech 4th Semester'
print(student1.__dict__)
# Removing the student_name attribute :
delattr(student1,"student_name")
print("Displaying object after deleting an attribute : ")
print(student1.__dict__)
