#-*-coding=utf-8-*-
'''
题目：
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''
# def func1(x):
# 	b = str(x)
# 	d = len(b)
# 	for x in b:
# 		if x != b[d - 1]:
# 			return False
# 		else:
# 			d -= 1
# 	return True

# def func2(x):
# 	a = str(x)
# 	b = a[::-1]
# 	if a == b:
# 		return True
# 	else:
# 		return False

def func3(x):
	a = str(x)
	L1 = [x for x in a]
	print(L1)
	L2 = list(a[::-1])
	print(L2)
	if L1 == L2:
		return True
	else:
		return False

if __name__ == '__main__':
	a = 12321
	c = func3(a)
	if c:
		print('这是一个回数')
	else:
		print('这不是回数')