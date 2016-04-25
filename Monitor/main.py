#!/usr/bin/python  
# -*- coding: utf-8 -*-  
'''
Created on 2016年4月25日

@author: jarekzhang
'''

from flask import Flask
from Monitor import jdItemPage


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    #app.run()
    jdItemPage.ReadAllFromMysql()
