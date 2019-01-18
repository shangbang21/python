# -*-coding = utf-8 -*-

"""
函数说明:用循环的方式生成指定不重复的三位数，列表数字按从小到大返回
Parameters:三位数中的最大值（num）
Returns:生成数字的LIST（L）
Modify:2019-01-09
"""
def numbers1(num):
	L = []
	for x in range(1, num):
		for y in range(1, num):
			for z in range(1, num):
				if x != y and x!= z and y != z:
				 	L.append(x * 100 + y * 10 + z)
	sorted(L, reverse = False)
	return L



"""
函数说明:用列表生成式的方式生成指定不重复的三位数，列表数字按从大到小返回
Parameters:三位数中的最大值（num）
Returns:生成数字的LIST（L1）
Modify:2019-01-09
"""
def numbers2(num):
	L = [x*100+y*10+z for x in range(1,num) for y in range(1,num) for z in range(1,num) if x != y and x!= z and y != z]
	L1 = sorted(L, reverse = True)
	return L1

if __name__ == '__main__':
	num = input('输入数字：')
	num = int(num)
	L2 = numbers1(num)
	L3 = numbers2(num)
	s1 = (len(L2) + len(L3)) // 2
	print('\n','共有数字：%s个' % s1,'\n','方法1得到的结果是:',L2,'\n','方法2得到的结果是:',L3)
