#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging

import cgitb
cgitb.enable()
import sys

print("Content-Type: text/plain;charset=utf-8")
print()

print("Hello, world!")
import os
sys.path.append('/home/yuuriapple/127.0.0.1/lib/python3.8/site-packages')

import cgi
form = cgi.FieldStorage(keep_blank_values = True )

import MySQLdb
# 接続する
con = MySQLdb.connect(
            user='test',        #作った全権限のuser名
            passwd='sYstem!6735',       #その時のPW
            host='127.0.0.1',   #ここは触らないでいいかも
            db='bord',        #db名
            charset="utf8")     #触らない
    # カーソルを取得する
cur= con.cursor()

#INSERT
cur.execute("INSERT INTO board_tb VALUES (NULL, 'yuuri' , 'yes' , '2020-06-02 14:45')")

# プレースホルダの使用例
cur.execute("INSERT INTO board_tb VALUES (NULL, 'jun' , 'no' , '2020-06-02 14:46')")
cur.execute("INSERT INTO board_tb VALUES (NULL, 'kei' , 'nothing' , '2020-06-02 14:47')")
cur.execute("INSERT INTO board_tb VALUES (NULL, 'nao' , 'somethig' ,  '2020-06-02 14:48')")
con.commit()


cur.close()
con.close()
