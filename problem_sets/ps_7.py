
#Team Manager 

class Player(object):
	
	def __init__(self, name, age, goals, jerseyNum, position):
		self.name = name
		self.age = int(age)
		self.goals = int(goals) 
    		self.jerseyNum = int(jerseyNum)
		self.position = str(position)
    
	def getPlayerSummary(self):
		summary = "Player Name: " + self.name + "\n"
		summary = summary + "Player Age: " + str(self.age) + "\n"
		summary = summary + "Goals Scored: " + str(self.goals) + "\n"
		summary = summary + "Jersey Number: " + str(self.jerseyNum) + "\n"
		summary = summary + "Position: " + self.position + "\n"
		return summary
	
	def attributeSplitter(self):
		sentence = self.name + " " + str(self.age) + " " + str(self.goals) + " " + str(self.jerseyNum) + " " + self.position + " " 
		return sentence 
	def loadTeam(playerList, filename):
					
		newList = first_player.split(' ')

		pass


def saveTeam(playerlist, filename):
	my_file =  open(filename, "w")
	for thing in playerlist:
		first_player = thing.attributeSplitter()
		my_file.write(first_player)
	my_file.close()
		

#ISIS EXECUTION STARTS HERE
players = []

#UI
keepRunning = True 

print("Welcome to Team Maneger Deluxe")

while keepRunning:
	print("Do you want to start with a new team or open an existing team?")
	print("Enter the number of your choice and press Enter.")
	print("(1) Start with a new team.")
	print("(2) Open a file for an existing team")
	# create variable for the optin the user picks
	response_1  = input()
	# a variable I will use to create a while loop after the user 
	#is trying to start a new team
	waffle = True
	if response_1 == 1:
		while waffle:
			print("What do you want to do? Enter the number of your choice and press Enter.")
			print("(1) Add a Player.")
			print("(2) Print all players.")
			print("(3) Save your player list to a file.")
			print("(0) Leave the program (save first to avoid losing your data!)")
			response_2 = input()
			if response_2 == 1:
				#options 
				print("Enter name:")
				pName = raw_input()
				print("Enter age:")
				pAge = input()
				print("Enter the number of goals scored this season.")
				pGoals = input()
				print("Enter the jersey number.")
				pJerseyNum = input()
				print("Enter the position.")
				pPosition = raw_input()
				myPlayer = Player(pName, pAge, pGoals, pJerseyNum, pPosition)
				players.append(myPlayer) 
				print("Ok, Player entered.")
			elif response_2 == 2:
				for things in players:
					print(things.getPlayerSummary())

			elif response_2 == 3:
				print("What do you want your Filename to be?")
				filename = raw_input() + ".tmd"
				saveTeam(players, filename)
			elif response_2 == 0:
				keepRunning = False 
				break

		
