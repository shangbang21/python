
#-*-coding=utf-8-*-
'''
题目：
从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
'''
# import os
file = open('97.txt','w')
s1 = ''
while True:
	a = input('一个字符')
	if a != '#':
		s1 += a
	else:
		file.write(s1)
		break
print(s1)
