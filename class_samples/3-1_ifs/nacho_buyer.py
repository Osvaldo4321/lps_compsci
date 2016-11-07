print("How much do the nachos cost?")

nacho_price = int(raw_input())

print("How much money do you have in your pocket?")
cash = int(raw_input())

if nacho_price > cash:
	print("Sorry, No Nachos for you :(")
if nacho_price <= cash:
	print("Woot, Nachos!")
if nacho_price == cash:
	print("That sure was lucky!")
print("Thanks for using nacho_buyer.py")
