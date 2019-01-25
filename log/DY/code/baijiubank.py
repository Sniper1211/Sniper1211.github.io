#!/usr/bin/python
# -*- coding: utf-8 -*-
start = int(input('输入开始号码:'))
end = int(input('输入结束号码:'))


def generateSerial(start, end):
    prefix = 'ZTCS0'
    comma = ','
    fo = open('test.txt', 'a+')
    while (start <= end):
        SerialNum = prefix + str(start) + comma
        fo.write(SerialNum)
        start += 1
    fo.write('\n')
    fo.write('*'*20)
    fo.write('\n')
    fo.close()



generateSerial(start, end)