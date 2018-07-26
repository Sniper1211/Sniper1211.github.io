#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1,10000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
# print(prod)