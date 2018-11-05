#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup



# 目标 url
url = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181015~20181021&dimensionid=78&rateType=1000"
# &filterNodes=23871%7C80

url42 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181015~20181021&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url43 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181022~20181028&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url44 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181029~20181104&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
# url 结尾不带 callback,正常值
def getProblem(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    # 发起请求
    re = requests.get(url, headers=headers)

    # Unicode 转换成中文
    decoded = re.text.encode('latin-1').decode('unicode_escape')

    soup = BeautifulSoup(decoded, 'html.parser')

    # 获取返回值,转成 str
    soup = str(soup)

    # 把 str 转换成 dict
    d = eval(soup)

    # 层层深入,找到热度排名的列表
    items = d['data']['results']['current']

    for item in items:
        i = item['item']
        v = item['value']
        r = item['rank']
        print(i, v, r)

#  url 结尾带上 callback
def getOrigin(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    # 发起请求
    re = requests.get(url, headers=headers)

    # Unicode 转换成中文
    decoded = re.text.encode('latin-1').decode('unicode_escape')

    soup = BeautifulSoup(decoded, 'html.parser')

    # 获取返回值,转成 str
    soup = str(soup)
    soup = soup[18:-2]

    # 把 str 转换成 dict
    d = eval(soup)

    # 层层深入,找到热度排名的列表
    items = d['data']['results']['current']

    for item in items:
        i = item['item']
        v = item['value']
        r = item['rank']
        print(i, v, r)


getOrigin(url42)
print('*'*50)
getOrigin(url43)
print('*'*50)
getOrigin(url44)