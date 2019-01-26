#!/usr/bin/python
# -*- coding: UTF-8 -*-

start = input('start:')
end = input('end:')

def generateNo(start, end):
    prifix = 'ZTCS0'
    comma = ','
    fo = open("foo.txt", "a+")
    while start <= end:
        num = start
        No = prifix + str(num) + comma
        fo.write(No)
        start += 1
    fo.write('\n'*2)
    fo.close()

generateNo(start,end)