import random

r = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	num = input('Guess a number: ')
	num = int(num)
	if num == r:
		print('You are right!')
		print('This is your', count, 'time guess.')
		break
	elif num > r:
		print('Answer is smaller')
	elif num < r:
		print('Answer is bigger')
	print('This is your', count, 'time guess.')