#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging

def main():

    import bbs
    import delete

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

    # 接続する
    con = MySQLdb.connect(
            user='test',
            passwd='sYstem!6735',
            host='127.0.0.1',
            db='bord',
            charset="utf8")     
    # カーソルを取得する
    cur= con.cursor()
    id=form.getvalue('id')
    sql = 'delete from board_tb where id=%s'
    cur.execute(sql, (id,))
    con.commit()

    cur.close()
    con.close()

    print("Content-Type: text/html; charset=utf-8\n")

    source = textwrap.dedent( '''
    <html>
    <head>
    <meta http-equiv="refresh" content=1; url="http://192.168.3.91/~yuuriapple/bbs.py">
    </head>
    <body>
    メッセージの削除に成功しました。
    </br>
    <form action ="bbs.py" method="post">
    <input type="submit" value="戻る"
    style=" background:pink;" "color:white;">
    </form>
    </body>
    </html>
    ''' )
    print(source)

if __name__ == "__main__":
    main()
