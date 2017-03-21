#create a blank Dictionary to store Information
myDictionary = {

}



#create a variable to the "True" function
hello = True 
while hello:
#User Interface
	print("(1) Add a phone number")
	print("(2) Print full list of contacts.")
	print("(3) Enter a name to retrieve that contact's phone number.")
	print("(4) Exit the contacts app.")
	answer = raw_input()
	#Options
	if answer == "1":
		print("Enter the name for the contact.")
		name = raw_input()
		print("Enter the contact's phone number.")
		number = raw_input()
		myDictionary[name] = number
		
	elif answer == "2":
		print myDictionary
		

	elif answer == "3":
		print("Whos contact do you want to print?")
		contact = raw_input()
		print(str(myDictionary[contact]))
	
	elif answer == "4":
		hello = False 
