#coding:utf-8
#!/usr/bin/env python
__author__ = 'dick'
from db.SQLiteHelper import SqliteHelper

sqlHelper = SqliteHelper()
cnt=sqlHelper.selectCount()
print cnt
sqlHelper.close()
