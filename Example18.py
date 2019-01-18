#-*-coding=utf-8-*-
'''
题目：
求s=a+aa+aaa+aaaa+aa...a的值，
其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

if __name__ == '__main__':
	a = int(input('输入要计算的数字：\n'))
	b = int(input('要相加到多少位？个1，十2，百3，千4，万5，十万6，百万，7'))
	sun = 0
	for x in range(b):
		sun += a
		a *= 10
		print(sun,end = ' ')
	print('\n',sun)
