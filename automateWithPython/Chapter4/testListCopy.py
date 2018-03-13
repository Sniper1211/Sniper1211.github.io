#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

aList = [1, 2, 3]
spam = ['A', 'B', 'C', 'D', aList]
cheese = copy.copy(spam)
cheese[1] = 42

deepCheese = copy.deepcopy(spam)
deepCheese[4] = [4, 5, 6]

print(spam)
print(cheese)
print(deepCheese)