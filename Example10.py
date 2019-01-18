#-*-coding=utf-8-*-
'''
题目：
暂停一秒输出，并格式化当前时间。
'''
import time
print(time.localtime())

print(time.strftime('%Y-%m-%d\n%H:%M:%S', time.localtime()))
time.sleep(2)
print(time.strftime('%Y-%m-%d\n%H:%M:%S', time.localtime()))

print(time.asctime(time.localtime()))