# -*- coding: utf-8 -*-
from random import random
from math import sqrt
from time import clock
DARTS = 1000000
hits = 1.0
clock()
for i in range(1,DARTS):
    x, y = random(), random()
    dist = sqrt(pow(x,2) + pow(y,2))
    
    if dist <= 1.0:
        hits += 1

pi = 4 * (hits/DARTS)
print pi
print "程序运行时间是" +  str(clock())+  "秒"
