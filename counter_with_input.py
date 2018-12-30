# code by Abhijeet Ghosh
# counts the numbers based on range and step from user

print("\t\tLet's get counting!!!")
print("\nTo start, please let me know the range and and steps between numbers")
print("\nAt any time to quit, just type 'exit'")

#get the starting number and keep prompting till a value is entered
start = ""
while not start:
    start = input("\nWhat number should I start from?\n")
    
#quit if user enters 'exit'
if start == "exit":
    exit()
    
#get the stopping number and keep prompting till a value is entered    
stop = ""
while not stop :
    stop = input("\nWhat number should I stop at?\n")

#quit if user enters 'exit'
if stop == "exit":
    exit()

#get the gap number and keep prompting till a value is entered     
step = ""
while not step:
    step = input("\nWhat is the gap between the numbers?\n")

#quit if user enters 'exit'
if step == "exit":
    exit()

print("\nAll right, let the counting begin!")

#sets up the counting range and prints the numbers
start = int(start)
stop = int(stop)
step = int(step)

count = range(start,stop+1,step)

print(*count)

input("\nPress Enter key to exit")
