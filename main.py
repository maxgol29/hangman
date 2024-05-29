from hanfman_words import word_list
from hangman_art import stages, logo
import random as r

print(logo)

random_word = word_list[r.randrange(len(word_list))]



def changing_user_word(letter, guess_word, input_word):
    for index in range(len(guess_word)):
        if letter == guess_word[index]:
            input_word[index] = guess_word[index]
    return input_word

def checker_of_letter(letter, guess_word):
    return letter in guess_word

def game(guess_word):
    attempts = 6
    user_word = ["_" for i in range(len(guess_word))]
    while attempts >= 0:
        guessed_symbol = input("Choose a letter: \n")
        correctness = checker_of_letter(guessed_symbol, guess_word)
        if correctness:
            print(*changing_user_word(guessed_symbol, guess_word, user_word))
            print(*[stages[attempts] if attempts < 6 else "You have full of attempts(7)!"])
        else:
            attempts -= 1
            if attempts < 0:
                print("You lost :(")
                break
            print(*user_word)
            print(stages[attempts])
        if ''.join(user_word) == guess_word:
            print("You won!!!")

game(random_word)


