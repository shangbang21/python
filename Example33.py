#-*-coding=utf-8-*-
'''
题目：
按逗号分隔列表。
'''
l1 = ['1','8','6','7','5']
l2 = [1,8,6,7,5]
l3 = '-'.join(str(x) for x in l2)
print(l3)