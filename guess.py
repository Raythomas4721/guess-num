import random
start = input('Please decide the random number start value')
end = input('Please decide the random number end value')
start = int(start)
end = int(end)
r = random.randint(start, end)
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