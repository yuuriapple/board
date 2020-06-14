#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging

def main():
    global id 
    global name
    global message
    global date
   
    import delete
    import delete1

    import cgitb
    cgitb.enable()
    import sys

    import textwrap
    import datetime

    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    import os
    sys.path.append('/home/yuuriapple/127.0.0.1/lib/python3.8/site-packages')

    import cgi
    form = cgi.FieldStorage(keep_blank_values = True )

    import MySQLdb

    id=form.getvalue('id')
    method=form.getvalue('method')

    print("Content-Type: text/html; charset=utf-8")  

    name= form.getvalue('name')
    message= form.getvalue('message')
    method= form.getvalue('method')

    #条件
    if(method == 'post'and (name == "" or message =="")):

                 print("""
                 <p id='error_message'>
                 もう一度入力してください</p>
                 """)

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

    #リダイレクト
    if(method == 'post'and not name == "" and not message ==""):
        source = textwrap.dedent( '''
        <html>
        <head>
        <meta http-equiv="refresh" content=1; url="bbs.py">
        </head>
        <body>
        メッセージの書き込みに成功しました。
        </br>
        </body>
        </html>
        ''' )
        print(source)


    # 接続する
    con = MySQLdb.connect(
            user='test',        #作った全権限のuser名
            passwd='sYstem!6735',       #その時のPW
            host='127.0.0.1',   #ここは触らないでいいかも
            db='bord',        #db名
            charset="utf8")     #触らない
    # カーソルを取得する
    cur= con.cursor()

    #表示
    cur.execute("select * from board_tb order by id desc;")
    rows = cur.fetchall()
    for row in rows:
        post_text=("""
        <div style = "border:solid;border-radius:900px;">
        <span style = "padding-left:30px;"></span>{name}
        <span style = "padding-right:500px;"></span>
        {date}
        <span style = "padding-right:300px;"></span>
        <form action ="delete.py" method ="post" style="display: inline">
        <input type="submit"value="削除" style=
       " background:blue;" "color:white;">
        <input type="hidden" name="id" value="{id}">
        <input type="hidden" name="name" value="{name}">
        <input type="hidden" name="message" value="{message}">
        <input type="hidden" name="date" value="{date}">
        </form>
        </br>
        <span style = "padding-left:30px;"></span>{message}
        </div>
        """ ).format(
        name=row[1],
        message=row[2],
        date=row[3],
        id=row[0]
        )
        print(post_text)
        name= form.getvalue('name')
        message= form.getvalue('message')
        method= form.getvalue('method')

    #条件
    if(method == 'post' and not name == "" and not message ==""):
        cur.execute('INSERT INTO board_tb (name, message) VALUES (%s, %s)',(name, message))
        con.commit()
        cur.close()
        con.close()

if __name__ == "__main__":
    main()
