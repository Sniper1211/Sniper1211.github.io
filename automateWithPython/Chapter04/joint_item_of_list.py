#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
假定有下面这样的列表：
spam = ['apples', 'bananas', 'tofu', 'cats']
编写一个函数，它以一个列表值作为参数，返回一个字符串。
该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入and。
例如，将前面的spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。
但你的函数应该能够处理传递给它的任何列表。
'''

spam = ['apples', 'bananas', 'tofu', 'cats']

def joint(spam):
    pre_string = ''
    for i in range(len(spam)-1):
        pre_string += str(spam[i]) + ','
    pre_string += 'and ' + str(spam[-1])
    print(pre_string)

joint(spam)