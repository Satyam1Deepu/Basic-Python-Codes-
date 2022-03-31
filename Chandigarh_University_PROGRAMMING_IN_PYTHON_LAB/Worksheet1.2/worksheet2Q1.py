""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

print(" Satyam Kumar deepu UID : 20BCS9274")
print("Enter number for Palindrome Check : ")
number = input()
# reverse Slicing :
reverseNumber = number[::-1]
# Flag :
dhindhora = False
i = 0
while( i < len(number)//2):
 if(number[i] != reverseNumber[i]):
   dhindhora = True
   break
 i += 1

if(dhindhora):
 print("Not a Palindrome Number")
else:
 print(" Paindrome Number : )")
