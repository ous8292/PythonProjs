import random
from words import words  # importing words from wordList file
import string

# some words have spaces or dashes.. so we need to choose a word from the list we can use


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' or ' ' in word:
        word = random.choice(words)

    return word.upper()

# we need to be able to keep track of letters we've guessed and which we have letters we have correctly guessed
# also need a way to keep track of what is a valid letter, and what is it


def hangman():
    # a variable that saves all the letters in a word as a set, to keep track of what's been guessed in the word
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    # using a predetermined list of capital letters in the english dictionary
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

  # getting user input
  # # lower case and upper case are different, so you cannot test equality
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join)['a', 'b', 'cd'] --> 'a b cd'
        print('You have used these letters ', ''.join(used_letters))

        # what the current word is (ie W-RD)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have used that letter. Try again')

        else:
            print('\nInvalid character. Try again')


# gets here when len(word_letters) == 0
    if lives == 0:
        print('You lost, the word was ', word)
    else:
        print('You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
