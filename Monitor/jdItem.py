#!/usr/bin/python  
# -*- coding: utf-8 -*-  
'''
Created on 2016年4月25日

@author: jarekzhang
'''
import mysqlConn
from ctypes.wintypes import SIZE

class JDItem(object):
    '''
    jd 商品页面
    '''
    _itemUrlFormat = u'http://item.jd.com/%s.html' 

    def __init__(self):
        '''
        Constructor
        '''
        self.itemID = None      # 物品ID
        self.itemName = None    # 物品名称
        self.price = None       # 价格
        self.inStock = None     # 是否有货
        self.time = None        # 时间  

    
def ReadAllFromMysql(itemID):
    '''
    从mysql中读出JDItemPage列表
    '''
    jdItemList = []
    conn = mysqlConn.MysqlConn()
    cursor = conn.getCursor()
    cursor.execute("select time,item_id,item_name,price,in_stock from item where item_id=%s order by time desc limit 100" % (itemID))
    results = cursor.fetchall()
    for row in results:
        jdItem = JDItem()
        jdItem.time = row[0]
        jdItem.itemID = row[1].decode('utf-8')
        jdItem.itemName = row[2].decode('utf-8')
        jdItem.price = row[3]
        jdItem.inStock= row[4]
        jdItemList.append(jdItem)
        
    return jdItemList
        
    
    
        