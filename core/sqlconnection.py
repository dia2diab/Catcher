#! /usr/bin/env python

import sqlite3
import os


class Connection(object):
    def __init__(self):
        self.db = os.getcwd() + "/core/db/db.db"
        if self.db:
            #print 'connecting to database ..'
            self.conn = sqlite3.connect(self.db)
            if self.conn:
                self.cur = self.conn.cursor()
                #print 'connection done.'

    def create(self):
        ''' this to create table for process'''
        for i in range(1, 3):
            table = self.tb_name(i)
            try:
                query = '''create table {0}(name text, \
                        path text, md5 text);'''.format(table)
                self.cur.execute(query)
                self.conn.commit()
                #print 'creating table {0} done.'.format(table)
            except sqlite3.OperationalError:
                #print 'table {0} already exist.'.format(table)
                pass

    def drop(self):
        ''' this to drop shots'''
        for i in range(1, 3):
            table = self.tb_name(i)
            query = 'drop table if exists {0}'.format(table)
            self.cur.execute(query)
            self.conn.commit()
        print '[+] droping shots tables .. [Done]'

    def into(self, kind, name=None, path=None, md5=None):
        ''' this to insert result to db '''
        table = self.tb_name(kind)
        query = '''insert into {0} (name, path, md5) \
                values ('{1}', '{2}', '{3}')'''.format(table, name, path, md5)
        #print query
        self.cur.execute(query)
        self.conn.commit()

    def getbymd5(self, kind, md5):
        ''' this to get file data by md5 '''
        table = self.tb_name(kind)
        query = '''select * from {0} where md5='{1}';'''.format(table, md5)
        data = self.cur.execute(query)
        if data:
            data = data.fetchall()
            return data

    def getAll(self, kind):
        ''' this to get all data from shots table '''
        table = self.tb_name(kind)
        query = ''' select * from {0} '''.format(table)
        data = self.cur.execute(query)
        self.conn.commit()
        data = data.fetchall()
        return data

    def close(self):
        self.conn.close()

    def tb_name(self, num):
        if num == 1:
            return 'catcher1'
        else:
            return 'catcher2'


#test = Connection()
#test.drop()
#test.create()
#test.into(1, 'ohhh', 'path', 'md5')
#test.into(1, 'ohhhh2', 'path', 'md6')
#print test.getbymd5(1, 'md5')
#test.close()
