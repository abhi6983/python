# code by Abhijeet Ghosh
# gets a message from user and prints it backwards

print("\t\tIT'S BACKWARDS DAY!!!")

#ask user for a message
message = str(input("\nplease enter a short message:\n"))

#calculate the length of the message
position = len(message)

#define the backwards variable
back = ""

#create the backwards text
while position > 0:
    back += message[position-1]
    position -= 1

#print the backwards variable    
print("\nThe message spelt backwards is :")
print(back.lower())

input("\nPress Enter to exit.")
