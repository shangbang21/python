#-*-coding=utf-8-*-
'''
题目：
利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
60分以下的用C表示。
'''

def level(level):
	if level >= 90:
		return 'A'
	elif level >= 60:
		return 'B'
	else:
		return 'C'


if __name__ == '__main__':
	score = int(input('输入成绩：\n'))
	if score > 100 or score < 0:
		print('输入错误！')
	else:
		level = level(score)
		print(level)
	


