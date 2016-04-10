#!/usr/bin/python  
# -*- coding: utf-8 -*-  
'''
Created on 2016年4月9日

@author: jarekzhang
'''
import urllib2
from lxml import etree
import json
from platform import system

class JDItemPage(object):
    '''
    JD商品页面
    '''
    
    ''' 价格 '''
    _priceUrlFormat = "http://p.3.cn/prices/get?skuid=J_%s"

    ''' 库存 '''
    _stockUrlFormat = 'http://c0.3.cn/stock?skuId=%s&cat=670,671,674&area=22_1930_50949_0&extraParam={"originid":"1"}'

    def __init__(self, url):
        '''
        Constructor
        '''
        self.url = url          # 页面地址
        self.itemID = None      # 物品ID
        self.itemName = None    # 物品名称
        self.price = None       # 价格
        self.inStock = None     # 是否有货        
        
        
    def parsePage(self):
        self._parseItemID()
        self._parseItemName()       
        self._parseItemPrice()
        self._parseItemStock()
    
        
    def _parseItemID(self):
        '''
        parse item id from page url
        '''
        urlSplit = self.url.split('/')
        endStr = urlSplit[len(urlSplit) - 1]
        endStrSplit = endStr.split('.')
        self.itemID = endStrSplit[0]
        
        
    def _parseItemName(self):
        pageContent = self._GetResponse(self.url)
        pageTree = etree.HTML(pageContent)
        itemNameNode = pageTree.xpath('//*[@id="root-nav"]/div/div/span[2]/a[2]')
        self.itemName = itemNameNode[0].text
    
    
    def _parseItemPrice(self):
        priceUrl = self._priceUrlFormat % (self.itemID)
        priceResponse = self._GetResponse(priceUrl)
        priceRspJson = json.loads(priceResponse)[0]
        self.price = float(priceRspJson['p'])        
        
        
    def _parseItemStock(self):
        stockUrl = self._stockUrlFormat % (self.itemID)
        stockUrlResponse = self._GetResponse(stockUrl)
        self.inStock = bool(stockUrlResponse.find(u'有货'))
    
    
    def _GetResponse(self, url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        pageContent = response.read().decode('GBK')
        return pageContent
        
        