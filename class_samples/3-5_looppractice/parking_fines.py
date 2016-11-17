#parking_fines.py

months = 0
ticket = 60

while ticket > 0:
	print("Have you paid your ticket? Yes/No.")
	response = raw_input()
	if response == "Yes":
		ticket = 0
	else:
		 ticket = ticket * 2
	print("Ok your ticket is now " + str(ticket))
