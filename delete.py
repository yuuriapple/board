#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging

def main():

    import bbs

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

    #id=form.getvalue('id')
    #name= form.getvalue('name')
    #message= form.getvalue('message')
    #date= form.getvalue('date')
    #print(id,name,message,date)

    print("Content-Type: text/html; charset=utf-8")
    id=form.getvalue('id')
    source = textwrap.dedent("""

    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <link rel="stylesheet"  href="delete.css">
    <body>
    <title>ひと言掲示板（投稿の削除）</title>
    </head>
    <h1>ひと言掲示板（投稿の削除）</h1>
    <form action ="bbs.py" method="post">
    <p class="text-confirm">以下の投稿を削除します。
    <br>よろしければ「削除」ボタンを押してください。</p>
    <div>
    <input id="btn" type="submit" name="btn_submit" value="キャンセル" 
    style=" background:white;" "color:black;">
    </form>
    <form action ="delete1.py" method="post">
    <input type="submit" value="削除"
    style=" background:blue;" "color:white;">
    <input type="hidden" name="id" value={a}>
    </form>
    </body>
    </head>
    </html>

    """ ).format(a=id)
    print(source)   

    id=form.getvalue('id')
    name= form.getvalue('name')
    message= form.getvalue('message')
    date= form.getvalue('date')
    print(id,name,message,date)

if __name__ == "__main__":
    main()
