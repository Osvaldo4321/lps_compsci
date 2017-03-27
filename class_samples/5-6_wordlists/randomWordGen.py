#imports random function
import random
#creates a variable for the file I want the comuter to READ off of. 
wordsFile = open('words.txt', 'r')

#Creates a blank list to store the words.
wordsList = []
#reads a line from words.txt
myWord = wordsFile.readline()

#while loop in order to read each line and re-assign the variable "myWord" to a new word.  
while myWord!= '':
        #as long as there are more words, put the word in the list and read another
        wordsList.append(myWord)
        myWord = wordsFile.readline()
#Counts how many things in list
wordsListLength = len(wordsList)

randomNum = random.randint(0,int(wordsListLength))

print(wordsList[randomNum])



