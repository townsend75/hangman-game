# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


name = input("Please enter your name here:")
print()
print(f"Welcome to Hangman, {name}!")
print()
print("Guess the secret word, one letter at a time")
print("If you think you have solved it, guess the word!")
print()
print("But beware: after 10 incorrect guesses, you lose!\n")
print()

words = ["kettle", "caterpiller", "antelope", "computer", "magnet",
         "telegraph", "telescope", "butcher", "tradition", "envelope",
         "trivial", "extraterrestrial", "sausage"]


def getRandomWord():
    # Retrieve a random word from the word list and
    # print hyphens corresponding to number of letters in word"""

    word = random.choice(words)
    print("Let's play hangman...\n")
    print("Fill in the blanks...\n")

    game(word)
    print()


def game(word):
    # The main game. Each chosen letter is evaluated until the word is
    # guessed or the number of triess reaches zero

    lettersGuessed = []
    wordsGuessed = []
    currentGame = list("-" * len(word))
    currentGame[0].split(",")
    guessed = False
    tries = 10

    print(*currentGame)
    print()
    print(f"You have {tries} tries remaining.")
    print()

    while not guessed and tries > 0:
        guess = input("Enter a letter of the alphabet...\n").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in lettersGuessed:
                print("You have already guessed this letter")
                print()

            elif guess not in word:
                print("This letter is not in the word")
                lettersGuessed.append(guess)
                tries -= 1
                print(f"You have {tries} tries remaining")
                print()
                print(f"You have already guessed these letters\n")
                print()
                print(*lettersGuessed)
                print()
                print(*currentGame)

            else:
                print(f"Good guess! {guess} is in the word:")
                lettersGuessed.append(guess)
                wordList = list(word)

                for index, letter in enumerate(wordList):

                    if letter == guess:
                        currentGame.pop(index)
                        currentGame.insert(index, guess)

                print()    
                print(*currentGame)
                print()

                if "-" not in currentGame:
                    print("Congrats, you won!")
                    print()
                    playAgain = input("Would you like to play again?\n(y/n)")
                    if playAgain == "y":
                        print()
                        getRandomWord()

                    else:
                        print("Thanks for playing!")
                        break          
          
        elif len(guess) == len(word) and guess.isalpha():
            if guess != word:
                print(f"Unlucky, {guess}  is not the word. Have another go")
                print()
                wordsGuessed.append(guess)
                print("You have already guessed these words:")
                print(*wordsGuessed)
                tries -= 1

            else:
                print("Congratulations! You solved the puzzle!")
                print()
                playAgain = input("Would you like to play again?\n(y/n)")
                print()
                if playAgain == "y":
                    print()

                    getRandomWord()
                else:
                    print("Thanks for playing!")
                    break     
        else:
            print("That is not a valid guess. Please try again")

        if tries == 0:
            print("Bad luck you lost!")


def main():

    getRandomWord()
  

main()
print()
print("\n")