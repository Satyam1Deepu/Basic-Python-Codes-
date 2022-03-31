""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

print(" Satyam Kumar deepu UID : 20BCS9274")
print("Enter number for Armstrong number Check : ")
number = input()
numberList = [int(i) for i in number]
length = len(numberList)
# Sum of Numbers :
sum = 0
i = 0
while( i < length):
    sum += numberList[i]**length
    i += 1
if(int(number)==sum):
    print(" Its an Armstrong number :)")
else:
    print(" Not an Armstrong number :(")
