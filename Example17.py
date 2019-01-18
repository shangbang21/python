#-*-coding=utf-8-*-
'''
题目：
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
import string

letters= 0
space = 0
digit = 0
others = 0
s = 'dsfjad#@#%!dsfjw38as0df dsgfw2gad9()'
x = 0
while x < len(s):
	if s[x].isalpha():
		letters += 1
	elif s[x].isspace():
		space += 1
	elif s[x].isdigit():
		digit += 1
	else:
		others += 1
	x += 1
print('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))