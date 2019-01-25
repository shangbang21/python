#-*-coding=utf-8-*-
'''
题目：
时间函数举例4，一个猜数游戏，判断一个人反应快慢。
'''
import time, random
a = random.randint(1,8)

# b = int(input('输入：'))


for x in range(3):
	b = int(input('输入：'))
	if a == b:
		print('恭喜！')
		break
	elif a > b:
		print('再大一点！')
	else:
		print('再小一点！')