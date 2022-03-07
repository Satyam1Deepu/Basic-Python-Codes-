""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

def printKFreqWords(s,k):
    words = s.split()
    dict = {}
    for word in words:
        dict[word] = dict.get(word, 0) + 1

    for word in dict:
        if dict[word] == k:
            print(word)

# Base code for functional Programming :
print("Enter string for which you want to get words with specific frequency : ")
givenString = input()
print("Enter Frequency : ",end =" ")
frequency = int(input())
printKFreqWords(givenString,frequency)
