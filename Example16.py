#-*-coding=utf-8-*-
'''
题目：
输出指定格式的日期。
'''
import time
print(time.localtime())
print(time.strftime('%Y-%m-%d', time.localtime()))
print(time.asctime(time.localtime()))