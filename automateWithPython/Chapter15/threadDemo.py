#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading, time
print('Start of program.')

def takeAnap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeAnap())
threadObj.start()

print('End of program.')