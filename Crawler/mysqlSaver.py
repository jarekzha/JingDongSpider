#!/usr/bin/python  
# -*- coding: utf-8 -*-  
'''
Created on 2016年4月11日

@author: jarekzhang
'''

import MySQLdb
import config

class MysqlSaver(object):
    '''
    save jdItemPage with mysql 
    '''

    def __init__(self):
        self.conn = MySQLdb.connect(config.MYSQL_HOST, config.MYSQL_USER, config.MYSQL_PASSWD, config.MYSQL_DB)
        self.conn.set_character_set('utf8')

    
    def execute(self, jdItemPage):
        cursor = self.conn.cursor()
        
        insertSql = jdItemPage.sqlInsertStr()
        cursor.execute(insertSql)
        
        self.conn.commit()
        cursor.close()


    def __del__(self):
        self.conn.close()