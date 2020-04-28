import random
answer = random.choice(range(1, 20))
question = "What number am I thinking of?  "
print ("Let\'s play the guessing game!")
while True:
	inp = input(question)
	try:
		guess = int(inp)
	except ValueError:
		print('Your guess should be a number')
	else:
		if guess < answer:
			print ('Little higher')
		elif guess > answer:
			print ('Little lower')
		else: # guess == answer
			print ('MINDREADER!!!')
			break
