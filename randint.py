#!/usr/bin/env python
import xlwt
from datetime import datetime

import random
import time
import math
import json
import pprint
import urllib2
x = 0
c = 0
bu = 0
na = 0
se = 0
while x < 100:
    def subtract(a, b):
        return a - b
    a = random.randrange(1, 10)
    b = random.randrange(1, 10)
    if a == b:
        na = na + 1
    if a > b:
        c = subtract(a,b)
        bu = bu + 1
        

    if a < b:
        se = se + 1
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True
    style0 = xlwt.XFStyle()
    style0.font = font0
    style1 = xlwt.XFStyle()
    style1.num_format_str = 'D-MMM-YY'
    wb = xlwt.Workbook()
    ws = wb.add_sheet('GOOG')
    ws.write(0, 0, 'Buy')
    ws.write(0, 1, 'Sell')
    ws.write(0, 2, 'No Change')

    #ws.write(0, 2, 'Date')
    ws.write(1, 0, bu)
    ws.write(1, 1, se)
    ws.write(1, 2, na)


    wb.save('stocks.xls')

    x = x + 1
print ("Done!")
