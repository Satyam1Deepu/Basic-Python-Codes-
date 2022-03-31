"""Python program to check whether the string is Symmetrical or Palindrome """

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

# Two Pointer Approach :
print('Satyam Kumar Deepu : 20BCS9274')
print("Enter string for Palindrome check : " , end = " ")
line = input()
 # flag :
isPalindrome = True
i , j = 0 , len(line) - 1
while( i < len(line)//2):
    if(line[i]== line[j]):
        i += 1
        j -= 1
    else:
        isPalindrome = False
        break

if(isPalindrome):
    print(" String is Palindrome :) ")
else:
    print(" String is not Palindrome :( ")
