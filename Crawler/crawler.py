#!/usr/bin/python  
# -*- coding: utf-8 -*-  
'''
Created on 2016年4月9日

@author: jarekzhang
'''
import urllib2
import config

if __name__ == '__main__':
    ''' 请求数据 '''
    request = urllib2.Request(config.URL)
    response = urllib2.urlopen(request)
    content = response.read()
    
    ''' 写日志 '''
    with open(config.LOG_FILE, 'w') as logFile:
        logFile.write(content)
    
    