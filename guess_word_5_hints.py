# code by Abhijeet Ghosh
# computer picks random word from list and user has to guess
# user gets 5 chances to ask is a letter is in the word

print("\t\tLet play a guessing game!")
print("\nYou will get 5 attempts to check if a letter is in the word")
print("\nAfter the 5th attempt, you will have to guess the correct word")

import random

# creates a list of words to choose from
WORDS = ("ancient",
         "history",
         "backward",
         "dictionary",
         "sequence")

# choose a random word from the WORDS list
pick = random.choice(WORDS)

# gives 5 tries to the user to input a letter to check
tries = 5

while tries > 0:
    guess = str(input("\nPlease enter only a single letter to check: "))
    tries -= 1            
    while len(guess) > 1 or guess == "":
        guess = str(input("\nPlease enter only a single letter to check: "))
    if guess.lower() in pick:
        print("\nYes,",guess.upper(),"is in the word.")
    else:
        print("\nNo,",guess.upper(),"is NOT in the word.")

#asks the user to enter the answer
ans = str(input("\nPlease enter your answer now:\n"))

#checks if user has answered correctly
if ans.lower() == pick:
    print("\nGreat! You correctly guessed that the word is :",pick)
else:
    print("\nSorry! The correct answer is :",pick)

input("\nPress the Enter key to exit")

