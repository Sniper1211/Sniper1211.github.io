#!/usr/bin/python
# -*- coding: utf-8 -*-

tableData = [
    ['apples', 'oranges', 'cherries', 'banna'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            if colWidths[x] < len(tableData[x][y]):
                colWidths[x] = len(tableData[x][y])
    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            if x == 0:
                print(tableData[x][y].rjust(colWidths[x]), end=' ')
            else:
                print(tableData[x][y].ljust(colWidths[x]), end=' ')
        print()

printTable(tableData)