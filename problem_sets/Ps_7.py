#Team Manager 
#creates a class for a Player.
#This "Player" class will store the Player's name, age, goals, jersey-number, and the position they play. 
class Player(object):
	
	def __init__(self, name, age, goals, jerseyNum, position):
		# assigning the parameters
		self.name = name
		self.age = int(age)
		self.goals = int(goals) 
    		self.jerseyNum = int(jerseyNum)
		self.position = str(position)

	#Creates a METHOD for the Player Class.
	#This method allows us to get a player summary of the object. 
	def getPlayerSummary(self):
		summary = "Player Name: " + self.name + "\n"
		summary = summary + "Player Age: " + str(self.age) + "\n"
		summary = summary + "Goals Scored: " + str(self.goals) + "\n"
		summary = summary + "Jersey Number: " + str(self.jerseyNum) + "\n"
		summary = summary + "Position: " + self.position + "\n"
		return summary

	#Method for Player Class
	#This method splits the attributes of a Player Object.
	def attributeSplitter(self):
		sentence = self.name + " " + str(self.age) + " " + str(self.goals) + " " + str(self.jerseyNum) + " " + self.position + '' + "\n" 
		return sentence 


#creates a GLOBAL function
#This function Loads/ opens an already existing file for this program to read. 
def loadTeam(playerList, filename):
	my_file = open(filename, 'r')
	#This function reads line by line
	kev = my_file.readline()
	while kev != "": 
		playerStats = kev.split(' ')
		#each line that hold information get split by a space
		#Each bit of info is split and set equal to an attribute within the player object.
		newPlayer = Player(playerStats[0], playerStats[1], playerStats[2], playerStats[3], playerStats[4])
		playerList.append(newPlayer)
		kev = my_file.readline()	
	my_file.close()

#Saveteam is also a GLOBAL function. 
#this function opens a new file and "writes" to it. 
def saveTeam(playerlist, filename):
	my_file =  open(filename, "w")
	for thing in playerlist:
		first_player = thing.attributeSplitter()
		my_file.write(first_player)
	my_file.close()
		

#ISIS EXECUTION STARTS HERE
players = []

#UI

print("Welcome to Team Maneger Deluxe.")
print("Do you want to start with a new team or open an existing team?")
print("Enter the number of your choice and press Enter.")
print("(1) Start with a new team.")
print("(2) Open a file for an existing team.")
# create variable for the optin the user picks
response_1  = input()

#if the user inputs the value of 2, the "loadTeam" funtion will run after you tell it what file to open.
if response_1 == 2: 
	print("Enter the name of the file you want to open. The computer will add .tmd")
	something = raw_input() + ".tmd"
	loadTeam(players, something)




# a variable I will use to create a while loop after the user is trying to start a new team
#variable waffle is just a place holder. 

waffle = True

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



