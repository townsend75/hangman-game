# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


name = input("Please enter your name here: \n")
print(f"Welcome to Hangman, {name}!")
print("Guess the secret word, one letter at a time")
print("But beware: after 10 incorrect guesses, you lose!")

words = ["kettle", "caterpiller", "antelope", "computer", "magnet",
         "telegraph", "telescope", "butcher", "tradition", "envelope", 
         "trivial", "extraterrestrial", "sausage"]


def getRandomWord():
    """Retrieve a random word from the word list and 
    print hyphens corresponding to number of letters in word"""

    word = random.choice(words)
    guessWord = "- " * len(word)
    print("Guess the word...")
    print(guessWord)

def userGuess():
    """Evaluate user guess"""
    userInput = ""

    while True:

        userInput = input("Enter a single letter\n").lower()

        if userInput.isalpha() and len(userInput) == 1:
            print(userInput)
            break
        else:
            print("You may only enter a single letter of the alphabet!")
            print("Please try again")




     
    

    



getRandomWord()
userGuess()