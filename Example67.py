#-*-coding=utf-8-*-
'''
题目：
输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''
#方法1
l2 = [8,5,9,16,7]
print(l2)
a = max(l2)
b = min(l2)
l2.remove(max(l2))
l2.remove(min(l2))
l2.insert(0,a)
l2.append(b)
print(l2)

#方法2
l2 = [8,5,9,16,7]
c = l2.index(max(l2))
d = l2.index(min(l2))
max = l2[c]
min = l2[d]
print(max, min)
l2.pop(c)
l2.pop(d)
l2.append(min)
l2.insert(0,max)
print(l2)