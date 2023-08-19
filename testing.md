# Testing

## PEP8 Python Validator

The code was run through the PEP8 Python validator and received the result "all clear, no errors found"

[Link to validator result](images/Python%20validator%20result.jpg)

## User testing

| Action | Expected result | Actual result |
| input name | Name appears in greeting| works as expected|
|input number | warning that the input is incorrect| works as expected|
| input two letters |warning that the input is incorrect| works as expected|
| input single letter which appears in solution | letter should be added to blank word and user informed of correct guess| works as expected|
| input letter which is not in solution | letter should be added to guessed letters list and user informed of incorrect guess. Tries should decrease by one | works as expected|
| input letter which has already been guessed | user is told they have already guessed letter | works as expected|
| input final letter of solution | message to congratulate user. Offer to play again | works as expected
|input word guess identical in length to solution but incorrect | user informed word is incorrect Word added to list of guessed words. Tries decrease by one | Works as expected|
|input word which has already been guessed | User told word has already been guessed. Show guessed word list | works as expected|
| input correct word | message to congratulate user. Offer to play again | works as expected|
| play again? y | game restarts| works as expected|
 | play again? n | message: thank you for playing | works as expected

 
