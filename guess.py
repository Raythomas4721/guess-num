import random

r = random.randint(1, 100)
while True:
	num = input('Guess a number: ')
	num = int(num)
	if num == r:
		print('You are right!')
		break
	elif num > r:
		print('Answer is smaller')
	elif num < r:
		print('Answer is bigger')