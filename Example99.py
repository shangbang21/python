#-*-coding=utf-8-*-
'''
题目：
有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
'''
file = open('99.txt','w')
file1 = open('99-1.txt')
file2 = open('99-2.txt')
s1 = ''
s1 = file1.read() + file2.read()
file.write(s1)