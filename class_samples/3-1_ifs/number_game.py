fav = 25 
print("Try and guess MY number between 1 and 50!")
user_number = int(raw_input())

if user_number > fav:
	print("Sorry, you loose :(")
	print("Try again: Next Time, try a little lower number")
if user_number == fav:
	print("Hooray, You won! Good Choice :3")
if user_number == 5:
	print("Hint: That number is a multiple and divisor of MY number.")
if user_number < fav:
	print("Try again: Next Time, try a little higher number")
