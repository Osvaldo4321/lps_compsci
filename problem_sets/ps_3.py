print("Welcome to your quest, *cough* *cough* your demise.")
print("What is you your name?")
name = raw_input()

if len(name) >= 7:
	print("Holy crap that's a cool name.")
else:
	print("lol, weak")

print("Anyways, Ok. Now, before we begin our quest, you are going to choose values for 3 character attributes.")
print("You will choose values for Strength, Health, and Luck. Keep in mind that the sum of all all you attributes should be a total of 15 points.")

print("Pick a value for Strength.(A value betweeen 1-10)")
Strength = int(raw_input())

print("Pick a value for Health.(A value betweeen 1-10)")
Health = int(raw_input())

print("Pick a value for Luck.(A value between 1-10)")
Luck = int(raw_input())


