
#-*-coding=utf-8-*-
'''
题目：
从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
'''
st1 = 'abcdefghijklmnopqrstuvwxyz'
st2 = st1.upper()
print(st2,st1)
file = open('98.txt', 'w')
file.write(st2)
file.close()