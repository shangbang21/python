#-*-coding=utf-8-*-
'''
题目：
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''
def fun(x):
	sum = 0
	if x % 2 == 0:
		y = 2
	else:
		y = 1
	while y <= x:
		sum += 1/y
		y += 2
	return sum

if __name__ == '__main__':
	a = int(input('输入一个数字：'))
	sum = fun(a)
	print(sum)