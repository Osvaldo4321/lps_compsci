""" number 2

print("How old are you?")
age = int(input())

print("How many inches tall are you?")
height = int(input())

if age > 10 and height > 50:
	print("Hooray! You're old enough and tall enough to ride.")
else:
	print("Sorry, you can't ride.")
""" 

print('Enter amount of purchases in cents')
price = int(raw_input())
price_discount = float(price * .1) 
dollars_spent = float((price + price_discount) / 100)
cents_spent = int(dollars_spent * 100)

if dollars_spent > 10:
	print('You spent over $' + dollars_spent + '!' + ' Your final price is' +  cents_spent + ' cents.')


if dollars_spent != 10:
	print('Your final price is' + cent_spent + ' cents.')
