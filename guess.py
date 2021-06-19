# 產生一個隨機整數1~100 (不印出)
# 讓使用者重複輸入數字猜
# 猜對, 印出"終於猜對"
# 猜錯, 印出"你的數字比答案大or小"
# 新增印出"這是你猜的第幾次"
# 新增讓使用者決定隨機整數的數字

import random
start = input('請決定隨機數字範圍的開始值')
end = input('請決定隨機數字範圍的結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1  # count = count + 1
	x = input ('請猜數字')
	x = int(x)
	if x == r :
		print('猜對了')
		print('這是你猜的第', count, '次')
		break
	elif x > r:
		print('你的數字比答案大')
	elif x < r:
		print('你的數字比答案小')
	print('這是你猜的第', count, '次')