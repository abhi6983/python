#assignment
#calculate price of the car

name = input("Hi, What's your name? ")

print("\nHello",name,end="")
print(", Nice to meet you.")
print("\nLet's calcualte the total price of the car.")

price = int(input("What is the base price of the car in US$?" ))

tax = price * 0.15
lic = price * 0.05
deal_prep = 200
dest = 10
print("\nThe tax on the car is $",tax)
print("The license fee on the car is $",lic)
print("The dealer prep charge on the car is $",deal_prep)
print("The destination charge on the car is $",dest)

print("\nThe total price of the car is $", price+tax+lic+deal_prep+dest)

input("\n\nPress the enter key to exit.")




