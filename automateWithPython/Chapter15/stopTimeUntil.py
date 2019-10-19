#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import time

Sunday_819 = datetime.datetime(2018, 8, 19, 16, 13, 50)
while datetime.datetime.now() < Sunday_819:
    time.sleep(1)
