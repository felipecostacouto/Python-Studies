import random

from codes.hangMan import hangman_words
from codes.hangMan.hangman_art import stages,logo


chosen_word = random.choice(hangman_words.word_list)

underscores = ["_"] * len(chosen_word)

print(logo)
print("The word as this length: ")
print('[', ', '.join(underscores), ']')

print("\nYour hangman, keep in alive bro")
print(stages[6])

n = len(stages) - 1
winner = True

while "_" in underscores:
    guess = input("\nMake a guess: ").lower()

    if guess in underscores:
        print(f'You\'ve already guessed {guess}')

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                underscores[index] = guess
        print(' '.join(underscores))

    else:
        n -= 1
        print("Motherfucker")
        print(stages[n])
        print(' '.join(underscores))
        if n == 0:
            print("You lost bro, loser")
            print("The word was " + chosen_word + ", but you lose")
            winner = False
            break

if winner:
    print("You made it bro, the word is: " + chosen_word)
