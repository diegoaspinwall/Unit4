#Diego Aspinwall
#10-23-17
#multiply.py

from random import randint

nicejob():
    

total = 0
while total<5:
    num1 = randint(1,12)
    num2 = randint(1,12)
    guess = int(input(num1, ' x ', num2,' = '))
    if num1*num2 == guess:
        total += 1
        nicejob()
    else:
        print('Sorry, incorrect')

