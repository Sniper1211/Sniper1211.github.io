#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 目标 url
url = "http://insight.baidu.com/base/search/rank/list?pageSize=20&source=0&toFixed=1&filterType=1&dateType=20181015~20181021&dimensionid=78&rateType=1000&filterNodes=23871%7C80&callback=_jsonp5xigt119is"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# 发起请求
re = requests.get(url, headers=headers)

# Unicode 转换成中文
decoded = re.text.encode('latin-1').decode('unicode_escape')

soup = BeautifulSoup(decoded, 'html.parser')
print(soup)
# 找到字典,之后遍历,找到具体的 value