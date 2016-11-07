# we're running an ACT prep class
# ask the user for their ACT score
# the ACT is scored as an integer out of 32 points
print("Hi! What's your SAT score?")
score = int(input())
 
 
if score <= 1300:
  print("Welcome to SAT prep class!")
elif score > 1300 and score < 1600:
  print("Thanks for coming, but you probably don't need this class.")
elif score == 1600:
  print("Whoa, you *really* don't need this class. Nice work.")
else:
  print("You must be lying. The top score on the SAT is 1600!")
