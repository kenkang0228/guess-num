# 產生一個隨機整數1~100 (不印出)
# 讓使用者重複輸入數字猜
# 猜對, 印出"終於猜對"
# 猜錯, 印出"你的數字比答案大or小"

import random
r = random.randint(1,100)
while True:
	x = input ('請猜數字')
	x = int(x)
	if x == r :
		print('猜對了')
		break
	elif x > r:
		print('你的數字比答案大')
	elif x < r:
		print('你的數字比答案小')