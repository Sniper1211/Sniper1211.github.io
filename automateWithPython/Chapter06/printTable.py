#!/usr/bin/python
# -*- coding: utf-8 -*-

tableData = [
    ['apples', 'oranges', 'cherries', 'banna'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
]

def printTable(tableData):
    #生成一个列表,包含三个子列表的长度,初始表示为0
    colWidths = [0] * len(tableData)

    #遍历第一个子列表的中每一项
    for y in range(len(tableData[0])):
        #遍历每个子列表
        for x in range(len(tableData)):
            #如果子列表的长度 小于 子列表内元素的长度
            if colWidths[x] < len(tableData[x][y]):
                #就取较大值
                colWidths[x] = len(tableData[x][y])

    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            if x == 0:
                print(tableData[x][y].rjust(colWidths[x]), end=' ')
            else:
                print(tableData[x][y].ljust(colWidths[x]), end=' ')
        print()

printTable(tableData)