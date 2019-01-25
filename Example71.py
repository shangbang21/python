#-*-coding=utf-8-*-
'''
题目：
编写input()和output()函数输入，输出5个学生的数据记录。
'''
class Student(object):
	"""docstring for Student"""
	# def __init__(self, name, gender, age):
	# 	self.__name = name
	# 	self.__gender = gender
	# 	self.__age = age

	def input(self):
		for x in range(3):
			if x == 0:
				self.__name = input('输入姓名：')
			elif x == 1:
				self.__gender = input('输入性别：')
			elif x == 2:
				self.__age = int(input('输入年龄：'))

	def output(self):
		for x in range(3):
			if x == 0:
				print(self.__name)
			elif x == 1:
				print(self.__gender)
			elif x == 2:
				print(self.__age)

if __name__ == '__main__':
	p1 = Student()
	p2 = Student()
	p3 = Student()
	l1 = [p1, p2, p3]
	for x in l1:
		x.input()
	for y in l1:
		y.output()