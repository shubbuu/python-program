import random

secretNumber = random.randint(1, 20)
print('Hi! Enter your name.')
name = input()

for x in range(1, 6):
    print('Guess a number which I have b/w 1 and 20')
    i = input()
    i = int(i)
    if secretNumber > i:
        print('yournumber is small')
    elif secretNumber < i:
        print('your number is high')
    else:
        break
if secretNumber == i:
    print('Your guess is correct')
else:
    print('your guess is incorrect')
