'''
题目：
输入某年某月某日，判断这一天是这一年的第几天？
（1）、非整百年：能被4整除的为闰年。（如2004年就是闰年,2001年不是闰年）
（2）、整百年：能被400整除的是闰年。(如2000年是闰年，1900年不是闰年)
'''


def runnian(x):
	if x % 400 == 0 or (x % 4 == 0 and x % 100):
		return True
	else:
		return False

def month(y):
	if y > 2:
		return True
	else:
		return False




if __name__ == '__main__':
	year = int(input('输入年：\n'))
	month = int(input('输入月：\n'))
	day = int(input('输入日：\n'))
	months = (0,31,59,90,120,151,181,212,243,273,304,334)
	sum = 0
	if 0 < month < 13:
		sum = months[month - 1] + day
	else:
		print('data error!')
	if runnian(year) and month(month):
		sum += 1
	print(sum)
