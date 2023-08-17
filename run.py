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


word = ""
guess = ""


def getRandomWord():
    """Retrieve a random word from the word list and 
    print hyphens corresponding to number of letters in word"""

    word = random.choice(words)
   
    #guessWord = "- " * len(word)
    print("Let's play hangman...")
    print(word)
    
    
    return word
    
    

"""def userGuess():
    Evaluate user guess
    letter = ""

    while True:

        letter = input("Enter a single letter\n").lower()

        if letter.isalpha() and len(letter) == 1:
            print(letter)
            break

        
            
        else:
                print("You may only enter a single letter of the alphabet!")
                print("Please try again")

    print(f"You guessed {letter}")
    return letter"""
    

           

def game(word): 

    lettersGuessed = []
    wordsGuessed = []
    currentGame = ["- " * len(word)]
    guessed = False
    tries = 10

    print(currentGame)
    print(f"You have {tries} tries remaining.")
    
    while not guessed and tries > 0:
        guess = input("Enter a letter of the alphabet...").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in lettersGuessed:
                print("You have already guessed this letter")

            elif guess not in word:
                print("This letter is not in the word")
                lettersGuessed.append(guess)
                tries -= 1
                print(f"You have {tries} tries remaining")
                print(lettersGuessed)
                print(currentGame)

            else:
                print(f"Good guess! {guess} is in the word:")  
                lettersGuessed.append(guess)
                gameList = list(word)
                for index, letter in enumerate(word):

                    if letter == guess:
                        gameList[index] = guess
                        currentGame.append(guess)
                
                
            
                print(gameList)   
                print(currentGame)
            
            
            
            
                            

        elif len(guess) == len(word) and guess.isalpha():
            if guess != word:
                print(f"Unlucky, {guess}  is not the word. Have another go")
                wordsGuessed.append
                print(wordsGuessed)

            else:
                print("Congratulations! You solved the puzzle!")    
            



        
              
        #else:
        #print("That is not a valid guess. Please try again")





            
           
    
def main():

    word = getRandomWord()
    #userGuess()
    game(word)

main()    

    




       
    
    
    
            
            










     
    

    

