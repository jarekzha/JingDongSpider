#!/usr/bin/python  
# -*- coding: utf-8 -*-  
'''
Created on 2016年4月25日

@author: jarekzhang
'''

import MySQLdb
import config
from common.singleton import singleton 

@singleton
class MysqlConn(object):
    '''
    conn object with mysql
    '''
    def __init__(self):
        self.conn = MySQLdb.connect(config.MYSQL_HOST, config.MYSQL_USER, config.MYSQL_PASSWD, config.MYSQL_DB)
        self.conn.set_character_set('utf8')
    
    #def __del__(self):
    #    self.conn.close()

    def getCursor(self):
        return self.conn.cursor()