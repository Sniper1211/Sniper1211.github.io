#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

string = input("Enter your string：")
repstr = input("Enter str which useless：")
def newstrip(str2,str1=''):
    # 定义x,y变量用于向正则中传递,x用于匹配原始字串开头的空白字符，y用于匹配原始字串结尾的空白字符
    x = '^\s*'
    y = '\s*$'
    # 如果用户没有输入将被删除的字串，那么就返回去除头尾空白字符的原始字串，否则返回被去除指定字串的新字串
    if str1 == '':
        newstr = re.sub(r'%s|%s'%(x,y),'',str2)
        print("删除字符串前后的空格")
    else:
        newstr = re.sub(str1,'',str2)
        print("字符" + str1 + "将从原始字串中被去除")
    return newstr
print("处理后的字串为：")
if repstr in string:
    print(newstrip(string,repstr))
else:
    print("你输入的字串不在原始字串中，或者不连续")