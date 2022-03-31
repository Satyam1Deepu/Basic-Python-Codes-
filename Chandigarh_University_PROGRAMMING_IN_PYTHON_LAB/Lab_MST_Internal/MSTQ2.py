print('\nSatyam Kumar Deepu : 20BCS9274')
def length(string):
    count = 0
    for char in string:
        count += 1
    return count

# Convert str1 to Uppercase letters
str1 = input("Enter string 1 : " ).upper()
str2 = input("Enter string 2 : " )
# Print the vowels in str2
print("Printing vowels from second string :")
for w in str2:
     if( w == "a" or w =="e" or w =="i" or w =="o" or w =="u"
     or w == "A" or w =="E" or w =="I" or w =="O" or w =="U"):
         print(w)
# Update str2 with your name
str2 = 'Satyam Kumar Deepu : 20BCS9274'
# Concatenate str1, str2
str3 = str1 + str2
#Display the Count of number of characters in both strings without using len function
print(str1)
print("Total number of characters in both strings : ",length(str3))
