import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('guess number: ')
	num = int(num)
	if num == r:
		print('you right!')
		print('第', count, '次猜')
		break
	elif num > r:
		print('over than the ans!')
	elif num < r:
		print('smaller than th ans!')
	print('第', count, '次猜')
