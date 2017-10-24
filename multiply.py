#Diego Aspinwall
#10-23-17
#multiply.py

from random import randint

nicejob():
    nice = randint(1,4)
    if nice == 1:
        print('Watch out world, here comes the next great multiplier!')
    if nice == 2:
        print('Nice fricking job dude')
    if nice == 3:
        print("You're better than Clay at multiplying")
    if nice == 4:
        print('Now try getting a job')

total = 0
while total<5:
    num1 = randint(1,12)
    num2 = randint(1,12)
    guess = int(input(num1, ' x ', num2,' = '))
    if num1*num2 == guess:
        total += 1
    else:
        print('Sorry, incorrect')

nicejob()