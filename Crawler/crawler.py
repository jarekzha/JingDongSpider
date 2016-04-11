#!/usr/bin/python  
# -*- coding: utf-8 -*-  
'''
Created on 2016年4月9日

@author: jarekzhang
'''

import config
from jdItemPage import JDItemPage
from mysqlSaver import MysqlSaver
import codecs
import time
  
if __name__ == '__main__':
    ''' 解析页面 '''
    itemPage = JDItemPage(config.URL)
    itemPage.parsePage()
    
    ''' 写日志 '''
    with codecs.open(config.LOG_FILE, 'a', 'utf-8') as logFile:
        infoStr = u'%s itemID:%s, itemName:%s, price:%s, inStock:%s \n' % (time.ctime(), itemPage.itemID, 
            itemPage.itemName, itemPage.price, itemPage.inStock)
        logFile.write(infoStr)
    
    saver = MysqlSaver()
    saver.execute(itemPage)
    

