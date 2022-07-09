import math
import random

print('Welcome to Guess The Number! \nThis is a game between the computer and user where the randomly selected number must be correctly guessed by either the computer or user. The range is defined by the user. Yes, that means you!')
print()

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Please pick a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, try again. Guess was too low.')
        elif guess > random_number:
            print('Sorry, try again. Guess was too high.')
    if guess == random_number:
        print()
        print(f'Congratulations!! You win! The randomly selected number was {random_number}.')

result = 0
def computer_guess(x): 
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low # or high, they are the same here. 
        feedback = input(f'Is {computer_guess} too high (H), too low (L), or correct(C)? ').lower()
        if feedback == 'l':
            low = computer_guess + 1
        elif feedback == 'h':
            high = computer_guess - 1
    if feedback == 'c':
        print()
        print(f'Computer has guessed your number, {computer_guess}, correctly!')

x = int(input('Enter the highest number to play with: '))
#guess(x)
computer_guess(x)