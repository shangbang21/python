#-*-coding=utf-8-*-
'''
题目：
字符串排序。
备注：先转list
'''

str1 = 'qwertyuiopasdfghjklzxcvbnm'
print(str1)
str2,str5 = list(str1),list(str1)
print(str2)
str2.sort()
print(str2)
str3 = sorted(str5)
print(str3)