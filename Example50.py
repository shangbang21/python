#-*-coding=utf-8-*-
'''
题目：
程序分析：使用 random 模块。
'''

import random
for x in range(10):
	x += 1
	print(random.randint(1,5) * x)