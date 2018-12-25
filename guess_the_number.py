# code by Abhijeet Ghosh
# guesses the random number selected by user

print("\t\tHello, let's play a game")
print("\nChoose a number between 1 and 100, but don't tell me.")
input("\nPress Enter key to start the game.")

import random

low = 1
high = 100

num = random.randint(low,high)

print("\nIs the number",num,"?")
ans = str(input("Yes or No?\n"))

while ans.lower() != "yes" and ans.lower() != "no":
    print("\nInvalid Response")
    print("\nIs the number",num,"?")
    ans = str(input("Yes or No?\n"))

# loop to keep generating the number till ans is no  
while ans.lower() != "yes":
    guess = str(input("\nDo I go 'higher' or 'lower'?\n"))
    if guess.lower() == "higher":
        low = num + 1
        num = random.randint(low,high)
    elif guess.lower() == "lower":
        high = num - 1
        num = random.randint(low,high)
    else:
        print("\nInvalid Response")
    
    print("\nIs the number",num,"?")
    ans = str(input("Yes or No? "))
    while ans.lower() != "yes" and ans.lower() != "no":
        print("\nInvalid Response")
        print("\nIs the number",num,"?")
        ans = str(input("Yes or No?\n"))
    
print("\nGreat! I knew I could guess the right answer.")

input("\n\nPress Enter key to exit.")
