#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import datetime

date_now = datetime.datetime.now()
# print(date_now)
this_week_start_date = str(date_now-datetime.timedelta(days=date_now.weekday())).split()[0]
this_week_end_date = str(date_now+datetime.timedelta(days=6-date_now.weekday())).split()[0]


# urltest = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20180806~20180812&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
urltest = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20180813~20180819&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"

# 目标 url

# url00 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType={}~{}&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc".format("2", "2")
url38 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181017~20180923&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url39 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20180924~20180930&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url40 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181001~20181007&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url41 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181008~20181014&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url42 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181015~20181021&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url43 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181022~20181028&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url44 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181029~20181104&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url45 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181105~20181111&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"
url46 = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181112~20181117&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp6g32mtviddc"

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
        print('test,', i+',', v)


getOrigin(url46)