#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

access_token = '2.00wlYL5BQNAUiB46f3a7d60eoLlaCB'
url = "https://api.weibo.com/2/statuses/share.json"
havetoUrl = 'http://genkit.cn'
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
    print(r.json())
else:
    print('发布成功，去查看吧')