import random
from words import words
import string

word = random.choice(words).upper()
# while '-' in word or ' ' in word:
#     word = random.choice(words)

def hangman():
    lives = int(len(word)) + 3
    word_letters = set(words) # Puts letters of word into a set
    alphabet = set(string.ascii_uppercase) # Set of all letters in upper case
    used_letters = set() # What user has guessed
    while len(word_letters) > 0 and lives > 1:
        print('You have ', lives, ' lives remaining, and the letters you have used are: ', ' '.join(used_letters)) # Prints what we have used
        word_list = [letter if letter in used_letters else '-' for letter in word] # Prints what the current word is, dashes where guesses remain
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: # If we have not guessed letter before
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives = lives - 1 
        elif user_letter in used_letters:
            print('You have guessed that letter before. Try again.')
        else: 
            print('Invalid entry. Try again.')
    if lives == 1:
        print('Last life! The letters you have used are: ', ' '.join(used_letters))
        print('Current word: ', ' '.join(word_list))
        guess_word = input('Guess the word: ').upper()
        if guess_word == word:
            print('Congratulations, you guessed the word!')
        else:
            print(f'You lose. The word was {word}.')
    else:
        print(f"Congrats you have guessed the word, {word}!")


hangman()