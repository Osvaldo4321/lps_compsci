print("For what numbers would you like multiples?")

num = float(raw_input())
multiple = 0 
last_num = 1

while last_num < 1000:
	last_num = num * multiple
	multiple = multiple + 1
	print( str(num) + " times " + str(multiple) + " is eqaul to " + str(last_num))
	if last_num >= 1000:
		print("That's all folks!")
		break
