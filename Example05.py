#-*-coding=utf-8-*-

def lappend(num):
	L = []
	x = 0
	while x < num:
		n = x + 1
		y = int(input('加入的数%s:'% n))
		L.append(y)
		x += 1
	return L


if __name__ == '__main__':
	num = int(input('加入几个数:'))
	L = lappend(num)
	L.sort(reverse = 0)
	L2 = sorted(L, reverse = 1)

	print('正序排列:',L)
	print('倒序排列:',L2)