# #-*-coding=utf-8-*-
# '''
# 题目：
# 写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度
# '''


def changdu(x):
	return len(x)


if __name__ == '__main__':
	a = input('输入字符串\n')
	b = changdu(a)
	print(b)
