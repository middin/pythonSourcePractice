# -*- coding: utf-8 -*-
# myStringIOp.py
# @author John Doe
# @description 
# @created Mon Oct 29 2018 13:52:03 GMT+0800 (CST)
# @last-modified Mon Oct 29 2018 14:06:37 GMT+0800 (CST)
#

from io import StringIO, BytesIO

f = StringIO('hello\nhi!\nworld!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f1 = BytesIO('中文'.encode('utf-8'))
print(f1.getvalue())
