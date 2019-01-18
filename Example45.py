#-*-coding=utf-8-*-
'''
题目：
统计 1 到 100 之和。
'''
su = 0
for x in range(1,101):
	su += x
print(su)
su = 0
x = 100
while x > 0:
	su += x
	x -= 1
print(su)
