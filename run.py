# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


name = input("Please enter your name here: \n")
print(f"Welcome to Hangman, {name}!")
print("Guess the secret word, one letter at a time")
print("But beware: after 10 incorrect guesses, you lose!\n")

words = ["kettle", "caterpiller", "antelope", "computer", "magnet",
         "telegraph", "telescope", "butcher", "tradition", "envelope", 
         "trivial", "extraterrestrial", "sausage"]

lettersGuessed = []
word = ""
guess = ""

def getRandomWord():
    """Retrieve a random word from the word list and 
    print hyphens corresponding to number of letters in word"""

    word = random.choice(words)
    
    #guessWord = "- " * len(word)
    print("Guess the word...")
    print(word)
    
    
    return word
    
    

def userGuess():
    """Evaluate user guess"""
    guess = ""

    while True:

        guess = input("Enter a single letter\n").lower()

        if guess.isalpha() and len(guess) == 1:
            print(guess)

        
            break
        else:
                print("You may only enter a single letter of the alphabet!")
                print("Please try again")

    #print(f"You guessed {guess}")
    return guess 
    

           

def game(word): 

    letterGuessed = []
    wordsGuessed = []
    currentGame = "- " * len(word)
    guessed = False
    tries = 10

    print(currentGame)
    print(guess)
    print(word)

    if guess in word:
        print(word)

    else:
        print("No way Jose")   
    
    
    
            
            










     
    

    



word = getRandomWord()
userGuess()
game(word)