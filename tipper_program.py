#assignment
#calculate the tip program

name = input("Hi, What's your name? ")

print("\nHello",name,end="")
print(", Nice to meet you.")
print("\nLet's calcualte the tip amount for your bill.")

bill = int(input("How much is the total bill?"))


tip_1 = bill * 0.15
tip_2 = bill * 0.20

print("\nThe tip amount at 15% is",tip_1)
print("So the total payment will be",bill + tip_1)
print("\nThe tip amount at 20% is",tip_2)
print("So the total payment will be",bill + tip_2)

input("\n\nPress enter key to exit.")





