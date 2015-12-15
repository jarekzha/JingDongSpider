# -*- coding: utf-8 -*-
import scrapy
from jingDongSpider import items

class ServerlistSpider(scrapy.Spider):
    name = "serverlist"
    allowed_domains = ["search.jd.com"]
    start_urls = (
        'http://search.jd.com/Search?keyword=%E6%9C%8D%E5%8A%A1%E5%99%A8&enc=utf-8&wq=%E6%9C%8D%E5%8A%A1%E5%99%A8', # 服务器搜索     
    )

    def parse(self, response):
        searshList = response.xpath('//*[@id="J_goodsList"]/ul/li')
        listItem = items.SearchListItem()
        return listItem
        
