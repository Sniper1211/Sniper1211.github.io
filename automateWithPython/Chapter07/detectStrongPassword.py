#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

passWord=str(input('Enter your password: '))

if len(passWord)<8:
    passWord=input('the length must be more than eight\n')
if re.compile(r'[A-Z]').search(passWord)==None:
    passWord=input('password must contain a Upper character at least.\n')
if re.compile(r'[a-z]').search(passWord)==None:
    passWord=input('password must contain a lower character at least.\n')
if re.compile(r'[0-9]').search(passWord)==None:
    passWord=input('password must contain digit\n')
else:
    print('proper password,congratulations')
