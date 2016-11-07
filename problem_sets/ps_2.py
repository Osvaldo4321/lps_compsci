print("How many people will you have at your party?")
people = int(raw_input())

print("How many donuts will you have at your party?")
doughnuts = int(raw_input())

doughnuts_per_person = doughnuts / people

print("Our party has " + str(people) + " people and " + str(doughnuts) + " doughnuts.")

print("Each person at the party gets " + str(doughnuts_per_person) + " doughnuts.")
 
