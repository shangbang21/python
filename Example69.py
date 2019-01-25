#-*-coding=utf-8-*-
'''
题目：
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
当成长不为1，设置跌代变量，用跌代变量对3取余，如果有余数，将列表第一个加到表尾，并删除第一个，当余数为0时，删除第一个。直到长度为1
'''
import time
l1 = list(range(0,34))
i = 1
print(time.gmtime())
while len(l1) != 1:
	if i % 3 != 0:
		l1.insert(len(l1), l1[0])
		l1.pop(0)
	else:
		l1.pop(0)
	i += 1
print(l1)
print(time.gmtime())

