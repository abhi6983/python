#code by Abhijeet Ghosh
# prints a list of words in random order without repetition

#creates a list of the words to choose from
WORDS = ["bronze", "innocent", "change", "authority", "contrary"]

import random

#loops through till WORDS is not empty and prints the words in random order once
while WORDS:
    sel = random.choice(WORDS)
    print("\n",sel)
    WORDS.remove(sel)

input("\nPress Enter to continue")
