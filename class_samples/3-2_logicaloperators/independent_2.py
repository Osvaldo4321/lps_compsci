
print('How many miles do you live away from Richmond?')
miles = int(raw_input())

print('What is your GPA?')
GPA = float(raw_input())

print("What's your ACT Score?")
ACT = int(raw_input())

if miles <= 30 and GPA >= 2.0:
        print("Congrats, you're in! Welcome to RN Richmond")
else:
        if miles >= 30 and ACT >= 18:
		 print('Welcome to CSU Richmond')
	else:
		print('Try CC')
