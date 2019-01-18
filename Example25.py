
#-*-coding=utf-8-*-
'''
题目：
求1+2!+3!+...+20!的和。
'''
sun = 1
num = 0
for x in range(1, 21):
	sun *= x
	num += sun
print(num)
