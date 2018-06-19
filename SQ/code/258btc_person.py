# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time, random, csv

# pageNum = '2797'
# 目前探明有效页码范围： 2415 - 3011

def getInfo(rawPageNum):
    try:
        pageNum = str(rawPageNum)
        resp = requests.get('http://www.528btc.com/person/'+ pageNum +'.html')

        soup = BeautifulSoup(resp.content, 'html.parser')

        name = soup.select('.name.marr10')[0].get_text()
        guest_info = soup.select('.guest_info')[0].get_text()
        img = soup.select('div.sidebar.right > div:nth-of-type(2) > img')[0].get('src')
        # 打印 人名、简介、照片
        print(name)
        print(guest_info)
        print(img)

        with open('/Users/lisinai/coding/sniper1211.github.io/SQ/result/data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            # writer.writerow(['id', 'name','description', 'img'])
            writer.writerow([pageNum, name, guest_info, img])
    except IndexError:
        with open('/Users/lisinai/coding/sniper1211.github.io/SQ/result/data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            # writer.writerow(['id', 'name','description', 'img'])
            writer.writerow([pageNum, '😝', '😝', '😝'])



for i in range(2415, 3012):
    print('*'*20)
    print(i)
    getInfo(i)
