from random import randrange 
number = randrange(1, 101)
tries = 0
guess = 0

while guess != number:
    guess = int(input('Guess a from 1 to 100: '))
    if number > guess :
        print('Too low, please try again')
    elif number < guess :
        print('Too high, please try again')
    tries += 1

print(f'{number} is the correct answer')
print(f'It took you {tries} to get the correct answer')