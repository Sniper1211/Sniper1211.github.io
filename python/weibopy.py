#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests

# url = "https://api.weibo.com/oauth2/access_token"
# payload ={
#     'client_id' : '1573442278',
#     'client_secret' : 'd120ecd272be3becb822d75abc4c3b9b',
#     'grant_type' : 'authorization_code',
#     'code' : '8a4cb5bc7513eee1567f491d3a011a4b',
#     'redirect_uri' : 'https://api.weibo.com/oauth2/default.html'
# }
#
# r = requests.post(url, data=payload)
# print(r.text)


access_token = '2.00wlYL5BQNAUiB836d43b2faMJaLHB'


url = "https://api.weibo.com/2/statuses/share.json"

payload={

    "access_token" : access_token,

    "status": '夜深了,班长在测试……星垂平野阔，月涌大江流http://genkit.cn'

}

files={
#
#     "pic":open("test.png", "rb")
#
}

r = requests.post(url, data=payload, files=files)
print(r.json())