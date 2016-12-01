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

print("Your name is " + name + ", your strength is " + str(Strength) + ", your health is " + str(Health) + ", and your luck is " + str(Luck))

print("Now that we have that all settled, lets continue on with your demise, I mean journey.")
print("*You travel along the yellow brick road only to be met by a fork in the road.*")
print("You have two options. You could either go left or right.")
print("You should hurry up and make your decision because I hear a bear coming.")

choice = raw_input()

if (choice == "Left" or choice == "left") and Strength >= 8:
	print("You went left and you were able to push a large boulder out of the way beacuse you were strong enough.")
	print("You follow the road only to be hit by a truck.")
	print("You lose, THE END!")
else:
	print("You went left and weren't able to push a large boulder out of the way because you are weak.")
	print("The bear caught up to you and made you vote for Donald Trump right before he ate you.")
	print("You died.")
	print("THE END!")

if (choice == "Right" or choice == "right") and Luck >= 7: 
	print("You are extremely Lucky that you automatically appear inside a castle and were crowed the King of the WORLD.")
	print("Seconds later, you get hit by a Bus. You LOSE!")
	print("The End!")
if (choice == "Right" or choice == "right" or choice == "Left" or choice == "left") and Health > 8:
	print("Since your Health is High, you survive everything.")
	print("Since you are practically immortal, You survive everything for so long that you outlived humanity and saw all your loved ones die.")
	print("Did you really win?")
	print("You are alone... But then again, aren't we all? .-.")
	print("THE END!")
