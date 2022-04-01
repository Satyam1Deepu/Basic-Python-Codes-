""""कर्मण्ये वाधिका रस्ते मा फलेषु कदाचन।
मा कर्म फल हेतु र्भूर्मा ते सङ्गोऽस्त्व कर्मणि॥"""

""" Satyam Kumar Deepu : 20BCS9274 """

testcase = int(input())
for i in range(testcase):
    lineTwo = input().split()
    numOfElement = int(lineTwo[0])
    X = int(lineTwo[1])
    Y = int(lineTwo[2])
    lineThree = input().split()
    lineThreeInInteger = [int(item) for item in lineThree]
    count = 0
    for element in lineThreeInInteger:
        if(element <= X and element%Y == 0):
            count += 1
    print(count)
