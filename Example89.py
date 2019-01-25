#-*-coding=utf-8-*-
'''
题目：
某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
加密规则如下：
每位数字都加上5,
然后用和除以10的余数
代替该数字，
再将第一位和第四位交换，
第二位和第三位交换。
'''
# x = 1860
# 6315
# 5136
a = 5136
st = list(str(a))
st.reverse()
i = 0
for x in range(4):
	b = int(st[x])
	if b > 4:
		b -= 5
	else:
		b = b + 10 - 5
	st.append(b)
print(st[-4:])

