# number 2
#Welcomes user to store and asks for age
print("Welcome to the convenience store!")
print("Enter your age:")
age = input()

age = int(age)
#if you're 18 years or older, tou can buy a lottery ticket and if you're less than 6 years old, you get a lollipop
if age >= 18:
  print("Would you like to buy a lottery ticket?")

if age < 6:
  print("Would you like to buy a lollipop?")
