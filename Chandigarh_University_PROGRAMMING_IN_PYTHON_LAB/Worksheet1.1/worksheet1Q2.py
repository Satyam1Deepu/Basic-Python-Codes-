""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

print("Enter marks of 5 subjects : ")
i = 0
totalMarks = 0
while( i < 5):
    totalMarks += float(input())
    i += 1
print(" Total marks of student is  : ",totalMarks,"/500")
print(" Average marks of student is  : ",totalMarks/5)
print(" Percentage  of student is  : ",(totalMarks*100)/500,"%")
