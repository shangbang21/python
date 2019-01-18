#-*-coding=utf-8-*-
'''
题目：
有5个人坐在一起，问第五个人多少岁？
他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
最后问第一个人，他说是10岁。请问第五个人多大？

'''
# a5 = 10
# for x in range(5 - 1):
# 	a5 += 2
# print(a5)  

# def function(x, y):
# 	if x == 1:
# 		return y
# 	else:
# 		return function(x-1,y + 2)

# if __name__ == '__main__':
# 	age = 10
# 	num = 1
# 	a_age = function(num,age)
# print(a_age)


def age(n):
	if n == 1:
		c = 10
	else:
		c = age(n-1) + 2
	return c

if __name__ == '__main__':
	print(age(5))