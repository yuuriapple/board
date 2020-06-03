#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging

import cgitb
cgitb.enable()
import sys

print("Content-Type: text/plain;charset=utf-8")
print()

print("Hello, world!")

import textwrap
import datetime

import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
sys.path.append('/home/yuuriapple/127.0.0.1/lib/python3.8/site-packages')

import cgi
form = cgi.FieldStorage(keep_blank_values = True )

import MySQLdb

print("Content-Type: text/html;charset=utf-8")  
print( """

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet"  href="form.css">
<body>
        <form action ="bbs.py" method="post">
<title>ひと言掲示板</title>
</head>
<h1>ひと言掲示板</h1>
<input type="hidden" name="method" VALUE="post">
<div>
        <label for="name">名前</label></br>
<input id="name" type="text" name="name" value="">
</div>
<div>
        <label for="message">メッセージ</label>
        </br>
        <textarea id="message" name="message"></textarea>
        </br>

<input id="btn" type="submit" name="btn_submit" value="書き込む" style=
       " background:hotpink;" "color:white;">
<hr>
</form>
<div>
<label for="name" type="text" name="name"value="">
</div>

</body>
</html>
     """ )
    # 接続する
con = MySQLdb.connect(
            user='test',        #作った全権限のuser名
            passwd='sYstem!6735',       #その時のPW
            host='127.0.0.1',   #ここは触らないでいいかも
            db='bord',        #db名
            charset="utf8")     #触らない
    # カーソルを取得する
cur= con.cursor()

#リダイレクト
def redirect():
            source =textwrap.dedent( '''
            <html>
                <head>
                    <meta http-equiv="refresh" content=0; url=./bbs.py">
                </head>
                <body>
                    メッセージの書き込みが完了しました。
                </body>
            </html>
            ''' )
            print(source)

#表示
cur.execute("select * from board_tb order by id desc;")
rows = cur.fetchall()
for row in rows:
        post_text=("""
        <div>
        <p style = border:solid; border-radius:8px;>
        <span style = padding-left:30px;></span>{name}
        <span style = padding-right:500px;></span>
        {date}
        </br>
        <span style = padding-left:30px;></span>{message}
        </p>
        </div>
        """ ).format(
        name=row[1],
        message=row[2],
        date=row[3],
        )
        print(post_text)
        name= form.getvalue('name')
        message= form.getvalue('message')
        method= form.getvalue('method')

#条件
if(method == 'post' and not name == "" and not message ==""):
        cur.execute('INSERT INTO board_tb (name, message) VALUES (%s, %s)',(name, message))
        con.commit()
        redirect()
elif(method == 'post'and (name == "" or message =="")):
                 print("""
                 <p id='error_message'>
                 もう一度入力してください</p>
                 """)

cur.close()
con.close()



