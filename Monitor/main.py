#!/usr/bin/python  
# -*- coding: utf-8 -*-  
'''
Created on 2016年4月25日

@author: jarekzhang
'''

from flask import Flask
from Monitor import jdItem


app = Flask(__name__)

@app.route('/')
def routeHelloWorld():
    return 'Hello World!'

@app.route('/item')
def routeItem():
    itemList = jdItem.ReadAllFromMysql(1019707)
    ret = ""
    for item in itemList:
        ret += (" %s" % (item.inStock))
        
    return ret
    
if __name__ == '__main__':
    app.run(debug=True)
