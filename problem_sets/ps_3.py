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

if Strength + Health + Luck > 15:
	Strength = 5
	Health = 5
	Luck = 5
	print("I told you that the total amount of attribute points you could have is 15. All attribute values have been set to 5")

print("Now that we have that all settled, lets continue on with your demise, I mean journey.")
print("*You travel along the yellow brick road only to be met by a fork in the road.*")
print("You have two options. You could either go left or right.")
print("You should hurry up and make your decision because I hear a bear coming.")

choice = raw_input()

if choice == "left" or choice == "Left":
	print("You've made a risky decision.")
if choice == "right" or choice == "Right":
	print("You've made the RIGHT decision ;)")

if (choice == "left" or choice == "Left") and Strength >= 7:
	print("You went left and you were able to push a large boulder out of the way beacuse you were strong enough.")
else:
	print("You went left and weren't able to push a large boulder out of the way.")
	print("The bear caught up to you and made you vote for Donald Trump right before he ate you.")
if (choice == "right" or choice == "Right") and Health >= 7: 
	
