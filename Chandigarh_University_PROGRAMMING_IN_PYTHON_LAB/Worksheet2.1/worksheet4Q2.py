"""Python program to find uncommon words from two Strings"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

# Taking both strings & spliting in single whitespace & returning list of words & then assigning into str 1 & str2 :
print('Satyam Kumar Deepu : 20BCS9274')
str1 = input("Enter string 1 : " ).split()
str2 = input("Enter string 2 : " ).split()

# Create 2  empty sets :

set1 = set()
set2 = set()

for i in str1 :
    set1.add(i)
for j in str2:
    set2.add(j)
#  ( A U B ) - ( A ∩ B ) <--> Symmetric  difference :
uncommonSet  = set1.symmetric_difference(set2)
# Printing Output :
print("Printing uncommon words from both strings : ")
for k in uncommonSet:
    print(k)
