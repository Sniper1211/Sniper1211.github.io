# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time, random

# pageNum = '2797'
# 目前探明有效页码范围： 2415 - 3011

def getInfo(rawPageNum):
    pageNum = str(rawPageNum)
    resp = requests.get('http://www.528btc.com/person/'+ pageNum +'.html')

    soup = BeautifulSoup(resp.content, 'html.parser')

    name = soup.select('.name.marr10')[0].get_text()
    guest_info = soup.select('.guest_info')[0].get_text()
    img = soup.select('div.sidebar.right > div:nth-of-type(2) > img')[0].get('src')

    print(name)
    print(guest_info)
    print(img)


for i in range(2433, 3011):
    print('*'*20)
    print(i)
    getInfo(i)
    # sleepTime = random.randint(1,10)
    # time.sleep(sleepTime)