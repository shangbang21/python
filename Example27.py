#-*-coding=utf-8-*-
'''
题目：
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''


def outstring(a,l):
	if l == 0:
		return
	print(a[l - 1])
	outstring(a,l - 1)
if __name__ == '__main__':
	a = '8760a'
	outstring(a,5)
