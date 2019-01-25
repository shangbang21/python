#-*-coding=utf-8-*-
'''
题目：
连接字符串。
'''
import random
st1 = 'song'
st2 = 'shang'
st3 = st1 + st2
print(st3)

ls1 = []
ls2 = []
for x in range(1,10):
	ls1.append('song'+ str(random.randint(1,20) + x))
	ls2.append('song'+ str(random.randint(1,20)))
print(ls1)
print(ls2)
ls3 = ls1 + ls2
print(ls3)