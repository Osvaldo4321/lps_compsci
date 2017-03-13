"""

#Question 1a

account_balance = 1000
 
withdrawal = 50
 
while account_balance > 0:
        print("Ok, your withdrawal has been made.")
        print("Your balance is now $" + str(account_balance - withdrawal) + ".")
	account_balance = account_balance - withdrawal

#Question 1b

bacteria_population = 1
minutes = 0
 
while bacteria_population < 5000000:
        print("After " + str(minutes) + " minutes, there are " + str(bacteria_population) + " bacteria in the sink.")
        print("No need to disinfect the sink yet.")
        bacteria_population = bacteria_population * 2
        minutes = minutes + 1
 
print("After " + str(minutes) + " minutes, there are " + str(bacteria_population) + " bacteria in the sink.")
print("You shoud use some Clorox on the sink now.")


#2

import random
myNum = random.randint(1,1000)

print("I am thinking of a number between 1-1000. Enter a guess!") 

guesses = 0
guess = int(raw_input()) 
while guess !=  myNum: 
        if guess > myNum: 
                print("Nope. Too high! Guess again.") 
                guess = int(raw_input())
		guesses = guesses + 1
        elif guess < myNum:
                print("Nope. Too low! Guess again.") 
                guess = int(raw_input())
		guesses = guesses + 1
if guess == myNum:
        print("Good job")
	guesses = guesses + 1
	print("It took you " + str(guesses) + " guesses.")

"""

print("Welcome To Pumapix")
print("Enter your favorite TV shows. Type 'Done' when you have finished.")

x = 0
shows = []

while x < 6:
	print("Enter a show name.")
	paper = raw_input()
	if paper == "done" or paper == "Done": 
		x = 10
	else:
		shows.append(paper)
	
print("Ok, this is what you entered: " + str(shows))
print("We've added a couple important ones.")


y = 1

more_shows = ['Breaking Bad', 'The Wire', 'The Walking Dead']


all = shows + more_shows

all.sort()


for things in all:
        print(str(y) + ". " + things)
        y = y + 1


