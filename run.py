# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


name = input("Please enter your name here: \n")
print(f"Welcome to Hangman, {name}!")
print("Guess the secret word, one letter at a time")
print("But beware: after 10 incorrect guesses, you lose!")

words = ["kettle", "caterpiller", "antelope", "computer", "magnet", "telegraph", "telescope", "butcher", "tradition", "envelope", "trivial", "extraterrestrial", "sausage"]


def getRandomWord():
    word = random.choice(words)
    guessWord = "- " * len(word)
    print(guessWord)


getRandomWord()