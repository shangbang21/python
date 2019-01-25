#-*-coding=utf-8-*-
'''
题目：
列表使用实例。

1	len(list)	列表元素个数
2	max(list)	返回列表元素最大值
3	min(list)	返回列表元素最小值
4	list(seq)	将元组转换为列表
序号	方法
1	list.append(obj)	在列表末尾添加新的对象
2	list.count(obj)		统计某个元素在列表中出现的次数
3	list.extend(seq)	在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)		从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)	将对象插入列表
6	list.pop([index=-1])	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)	移除列表中某个值的第一个匹配项
8	list.reverse()		反向列表中元素	
9	list.sort(cmp=None, key=None, reverse=False)	对原列表进行排序
10	list.clear()	清空列表
11	list.copy()		复制列表
'''
import random
list1 = [7,5,6,3,9,25,13,4]
a = len(list1)
print(a)
print(max(list1),min(list1))
tuple1 = (9,25,13,47,5,6,3)
list2 = list(tuple1)
print(list2)
for x in range(5):
	list1.append(x + random.randint(1,8))
print(list1)
print('3出现的次数：', list1.count(3))
list1.extend(list2)
print(list1)
print(list1.index(9))
list1.insert(0,list2)
print(list1)
list1.pop()
print(list1)
list1.pop(3)
print(list1)
list1.remove(list2)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list3 = list1.copy()
print(list3)
list3.clear()
print(list1)
print(list3)