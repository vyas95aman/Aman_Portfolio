import random

print('Welcome to Rock Paper Scissors!')
print()

hands = ['r', 'p', 's']

def play():
    user = input('Select rock (r), paper (p) or scissors (s): ').lower()
    computer = random.choice(hands)
    if user == computer:
        print("It's a tie!")
    elif win(user, computer):
        print('You win!')
    else:
        print('You lost!')
    replay = input('Want to play agian, Yes (y) or No (n)? ')
    if replay == 'y':
        play()
    else:
        print('Thank you for playing.')


def win(user, computer):
    # return true if player wins
    # r>s, s>p, p>r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

play()