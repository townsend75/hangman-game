# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

# The hangman class sets the variables which will be used during the game

class Hangman:

    def __init__(self, words, lettersGuessed, wordsGuessed, guessed, tries):
        self.words = words
        self.lettersGuessed = lettersGuessed
        self.wordsGuessed = wordsGuessed
        self.guessed = guessed
        self.tries = tries


# This section welcomes the player to the game
# and explains the rules.

print("-----------------------------------------------")

name = input("Please enter your name here: \n")

print((f"Welcome to Hangman, {name}, "
      "Guess the secret word, one letter at a time, "
       "If you think you have solved it, guess the word! "
       "But beware: after 10 incorrect guesses, you lose!"))


words = ["KETTLE", "CATERPILLER", "ANTELOPE", "COMPUTER", "MAGNET",
         "TELEGRAPH", "TELESCOPE", "BUTCHER", "TRADITION", "ENVELOPE",
         "TRIVIAL", "EXTRATERRESTRIAL", "SAUSAGE", "SOLIDIFY", "ASPARAGUS"]


def getRandomWord():
    # Retrieve a random word from the word list
    # and start the game function.

    word = random.choice(words)
    print("-----------------------------------------------")
    print()
    print(("Let's play hangman...\n"
          "Fill in the blanks...\n"))
    print(f"The word has {len(word)} letters.\n")

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
    print(f"You have {tries} tries remaining.\n\n")

    while not guessed and tries > 0:
        guess = input("Enter a letter of the alphabet...\n\n").upper()

        if guess.isalpha() and len(guess) == 1:
            if guess in lettersGuessed:
                print()
                print("You have already guessed this letter\n\n")

            elif guess not in word:
                print()
                print("This letter is not in the word\n\n")
                lettersGuessed.append(guess)
                tries -= 1
                print(f"You have {tries} tries remaining\n\n")
                print(f"You have already guessed these letters\n\n")
                print(*lettersGuessed)
                print()
                print(*currentGame)
                print()

            else:
                print()
                print(f"Good guess! {guess} is in the word: \n\n")
                lettersGuessed.append(guess)
                wordList = list(word)

                for index, letter in enumerate(wordList):

                    if letter == guess:
                        currentGame.pop(index)
                        currentGame.insert(index, guess)
                        print(*currentGame)
                        print()

                if "-" not in currentGame:
                    print("Congrats, you won!")
                    print()
                    playAgain = input("Would you like to play again?\n(y/n)\n")
                    if playAgain == "y":
                        print()
                        getRandomWord()

                    else:
                        print("Thanks for playing!")
                        break

        elif len(guess) == len(word) and guess.isalpha():
            if guess != word:
                print(f"Unlucky, {guess}  is not the word.\n\\n")
                wordsGuessed.append(guess)
                print("You have already guessed these words:\n\n")
                print(*wordsGuessed)
                tries -= 1

            elif guess in wordsGuessed:
                print()
                print("You have already guessed this word\n")
                print(*wordsGuessed)

            else:
                print("Congratulations! You solved the puzzle!")
                print()
                playAgain = input("Would you like to play again? \n(y/n)")
                print()
                if playAgain == "y":
                    print()

                    getRandomWord()
                else:
                    print("Thanks for playing!\n")
                    break
        else:
            print("That is not a valid guess. Please try again\n\n")

        if tries == 0:
            print("Bad luck you lost!\n\n")
            playAgain = input("Would you like to play again?\n\n(y/n)\n")
            if playAgain == "y":
                print()

                getRandomWord()
            else:
                print("Thanks for playing!\n")
                break


def main():
    # main function to restart the game after
    # first play.

    getRandomWord()


main()
print()
