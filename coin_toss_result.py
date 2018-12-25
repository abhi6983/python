# code by Abhijeet Ghosh
# simulates 100 coin tosses and tells the number of heads and tails

print("\t\tHello, Let the coin tosses begin!")
input("\nPress the Enter key to begin")

import random

toss = 0
head = 0
tail = 0

# randomly selects either 1 or 2 100 times and increments the count of head ot tail
while toss < 100:
    result = random.randint(1,2)
    if result == 1:
        head += 1
    else:
        tail += 1
    toss += 1

print("\nThe number of heads is", head, "and the number of tails is", tail)

input("\n\nPress Enter key to exit")
