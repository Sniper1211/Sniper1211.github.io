#!/usr/bin/python
# -*- coding: utf-8 -*-

print('Enter a number')
number = int(input())

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = number*3+1
            print(number)

collatz(number)