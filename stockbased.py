#!/usr/bin/env python
import xlwt
from datetime import datetime
import time
import math
import json
import pprint
import urllib2
x = 1
i = 1
c = 0
while i <6:

    while x < 10:
        
        def subtract(a, b):
            return a - b

        def get_stock_quote(ticker_symbol):   
            url = 'http://finance.google.com/finance/info?q=%s' % ticker_symbol
            lines = urllib2.urlopen(url).read().splitlines()
            return json.loads(''.join([x for x in lines if x not in ('// [', ']')]))


        if __name__ == '__main__':
            quote = get_stock_quote('goog')
#            print quote['l_cur']
            a = (quote['l_cur'])
            print (a)

            time.sleep(5)
            quote = get_stock_quote('goog')

            b = (quote['l_cur'])
            print (b)
        
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
    i = i + 6        
print ("Done!")
