import random
r = random.randint(1, 100)
while True:
	num = input('guess number: ')
	num = int(num)
	if num == r:
		print('you right!')
		break
	elif num > r:
		print('over than the ans!')
	elif num < r:
		print('smaller than th ans!')