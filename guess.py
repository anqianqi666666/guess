#產生一個隨機數1~100
#讓使用者重複輸入數字去猜
#猜對了, 印出"你答對了"
#猜錯了, 要告訴他比答案大還是小
import random
r  = random.randint(1, 100)
while True:
	num = input('請輸入數字')
	num = int(num)
	if num == r:
		print('correct')
		break
	elif num > r:
		print('bigger')
	elif num < r:
		print('smaller')