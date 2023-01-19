"""
import sales# it will ru sales.pyc file, it will create a frame called sales[create_customer,x,y]
import purchase# it will ru purchase.pyc file, it will create a frame called purchase[create_supplier,x,y]
sales.create_customer()
purchase.create_supplier()
print(sales.x)
print(purchase.x)

# create a folder. create three files. import two files functinos in to third file and call those functions in third file. Run the third file

import sales
import purchase
import stock

#import stock
from stock import stock_in, stock_out
stock_in.stockin()
stock_out.stockout()
"""
import sys
print(sys.path)
import deliver
