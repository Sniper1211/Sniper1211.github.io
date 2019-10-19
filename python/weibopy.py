#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

access_token = '2.00PQznvHYidrGE5ca33e0d7eNrTHiB'
url = "https://api.weibo.com/2/statuses/share.json"
havetoUrl = 'http://www.genkit.cn'
weiboContent = input('输入微博内容:')

payload={
    "access_token" : access_token,
    "status":  weiboContent + havetoUrl
}

files={
    # "pic":open("", "rb")
}

r = requests.post(url, data=payload, files=files)
if r.status_code != 200:
    print('发布失败')
else:
    print('发布成功，去查看吧')