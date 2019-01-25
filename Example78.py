#-*-coding=utf-8-*-
'''
题目：
找到年龄最大的人，并输出。请找出程序中有什么问题。
'''


dict1 = {'li':17,'zhao':16,'qian':19,'sun':12}

for x,y in dict1.items():
	print(x,y)
maxperson = max(dict1.values())
print('最大年龄', maxperson)
for x, y in dict1.items():
	if y == maxperson:
		print('最大的人是：',x,'年龄是：',y)
