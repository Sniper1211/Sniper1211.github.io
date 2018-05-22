#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
guess = ''
while guess not in ('head', 'tails'):
    print('Guess the coin tos! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')