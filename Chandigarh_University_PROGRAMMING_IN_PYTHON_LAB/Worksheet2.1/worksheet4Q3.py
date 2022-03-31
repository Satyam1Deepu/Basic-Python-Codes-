"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
Example:- Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly''"""

""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def suffixAdder(string ):
    # Edge Case :
    if (len(string) <= 2):
        return string

    elif( string[len(string) -3::1] =='ing'):
        str2 = string + "ly"
        return str2
    elif(string[len(string) -3::1]!= 'ing'):
       str3 = string + "ing"
       return str3

print('Satyam Kumar Deepu : 20BCS9274')

str1 = input('Enter string : ')
str1 = suffixAdder(str1)
print(str1)
