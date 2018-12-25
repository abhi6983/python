# assignment by Abhijeet Ghosh
# this simulates a fortune cookie prediction

print("\t\tHello, Let's see what your fortune says today!")
input("Press Enter key to open the Fortune Cookie")

import random

fortune = random.randint(1,5)

if fortune == 1:
    print("Some days you are pigeon, some days you are statue. Today, bring umbrella.")

elif fortune == 2:
    print("Two days from now, tomorrow will be yesterday.")

elif fortune == 3:
    print("Practice safe eating. Always use condiments.")

elif fortune == 4:
    print("A day without sunshine is like night.")

elif fortune == 5:
    print("The fortune you seek is in another cookie.")

else:
    print("No fortune for you today")

input("\n\nPress Enter key to Exit")
