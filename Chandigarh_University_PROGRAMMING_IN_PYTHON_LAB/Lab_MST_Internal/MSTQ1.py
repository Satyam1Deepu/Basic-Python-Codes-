print('\nSatyam Kumar Deepu : 20BCS9274')
num = int(input("Enter number for divisibility check : "))
i = 2
while( i <= 4):
    if(num%i==0):
        print(num,' is divisible by ',i)
    else:
        print(num, ' is not divisible by ', i)
    i += 1
