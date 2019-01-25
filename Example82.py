#-*-coding=utf-8-*-
'''
题目：
8转10
'''
def to10(num):
	print("8进制数：", num)
	l = str(num)
	length = len(l)
	print(length)
	sum = 0
	for i in range(length):
		sum += 8 ** i * int(l[length-1-i])
		print('sum:',sum)
	print("转成10进制数为：",sum)



if __name__ == '__main__':
	a = 152
	to10(a)
