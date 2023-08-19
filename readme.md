# Welcome to Hangman!

Hangman is a Python terminal game which runs in the Code Institute mock terminal on Heroku. 
Users can try and guess a random word, one letter at a time. After ten incorrect guesses, the player loses.

[View game on heroku here](https://hangman-townsend-c81a17acad8f.herokuapp.com/)
[View source code here](https://github.com/townsend75/hangman-game)


## How to play

The computer selects a random word from a list. The number of letters in the word is then displayed as blanks( dashes), allowing the user to see the number of letters in the word. 
The player is then asked to guess a letter. If the letter appears in the word, either once or multiple times, the blanks are replaced by the guessed letter(s) in the correct position. If the guessed letter is not in the word, the number of tries is reduced by one. 
At any time, the player can also try to guess the complete word. If they are wrong, they lose one try and continue the game. 

The player wins if they can guess the word within the allotted number of tries. 

## Features

-Firstly the player inputs their name:

![User name input](images/Hangman%20Enter%20name.jpg)

-They are then personally welcomed to the game and the rules are explained:

[Welcome message](images/Welcome%20message.jpg)

-Random word selection from list
- Validation errors for when input is not a letter of the alphabet
- Lists containg letters and words which have already been guessed
- Number of tries limited and counted down when guess is false
- Whether game is won or lost, player is asked if they would like to try again

[Link to play again question](images/Hangman%20Play%20Again.jpg)



## User Stories

If I were to implement this hangman game in a front end application, my target audience would be the casual user who wants to pass the time, maybe during a coffee break or waiting in a queue. The simplistic rules and relatively short time needed to complete a game lend themselves obviously to people who are killing a few minutes with their mobile devices or taking a break from working on a different application. 

### Future Considerations

In a front end application, I would include a score counter to keep track of games won and lost. I would also use a simple graphic of the hangman steps, as we know from the pen and paper game. The word list could also be expanded ad infinitum. 

## Credits

My mentor, Sherly Goldberg was very helpful n guiding me to the correct solution for replacing the blanks with a correctly guessed letter. 
I discovered the asterisk - print(*currentGame) - solution to remove parentheses from lists on the stackoverflow website. 
I use google a lot to check syntax if something doesn't work- the correect syntax for checking the length of a word, for example. 
The hangman idea came from a website listing first python project ideas. [link to website](https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/)

### Acknowledgements

Thanks again to my mentor, Sheryl, who always manages to calm me down and get me on the right track, without ever directly feeding me the answer!

