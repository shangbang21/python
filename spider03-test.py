# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
	f1 = open('taobao1.txt', 'w')
	f2 = open('taobao2.txt', 'w', encoding='utf-8')
	obj_req = requests.get('https://www.biqukan.com/1_1094/5403177.html')
	f1.write(obj_req.text)
	obj_bfs = BeautifulSoup(obj_req.text, features="html.parser")
	obj_bfs_txt = obj_bfs.find_all('div', class_ = 'content')
	f2.write(obj_bfs_txt[0].text.replace('\xa0'*8, '\n\n'))
	f1.close()
	f2.close()