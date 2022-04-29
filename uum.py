
import random
start = int(input('請使用者輸入開始值'))
end =int(input('請使用者輸入結束值'))
r = random.randint(start,end)
count = 0
while True:
	count = count + 1
	num = input('請輸入數子:')
	num = int(num)
	if num == r:
		print('你答對了')
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第幾次',count,'次')