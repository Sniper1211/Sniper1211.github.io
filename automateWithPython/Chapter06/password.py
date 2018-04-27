#!/usr/bin/python
# -*- coding: utf-8 -*-
#password.py - An insecure password locker program

import sys, pyperclip

PASSWORDS = {
    'email': 'F7minlBDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
}

if len(sys.argv) < 2:
    print('Usage: python3 password.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)