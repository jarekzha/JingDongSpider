#!/usr/bin/python  
# -*- coding: utf-8 -*-  
'''
Created on 2016年4月25日

@author: jarekzhang
'''
import mysqlConn
import MySQLdb

class JDItemPage(object):
    '''
    jd 商品页面
    '''
    _itemUrlFormat = u'http://item.jd.com/%s.html' 

    def __init__(self, params):
        '''
        Constructor
        '''
        self.url = None         # 商品URL
        self.itemID = None      # 物品ID
        self.itemName = None    # 物品名称
        self.price = None       # 价格
        self.inStock = None     # 是否有货
        self.time = None        # 时间  

    
def ReadAllFromMysql():
    '''
    从mysql中读出JDItemPage列表
    '''
    conn = mysqlConn.MysqlConn()
    cursor = conn.getCursor()
    cursor.execute("select time,item_id,item_name,price,in_stock from item order by time desc limit 100")
    results = cursor.fetchall()
    for row in results:
        print row 
    
    
        