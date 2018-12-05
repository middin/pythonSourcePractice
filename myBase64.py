#-*- coding: utf-8 -*-
# myBase64.py
# @author John Doe
# @description 
# @created Fri Nov 02 2018 11:55:26 GMT+0800 (CST)
# @last-modified Sat Nov 10 2018 14:05:36 GMT+0800 (CST)
#


import base64

print('\n')
print(base64.b64encode(b'binary\0x00string'))
print(base64.b64decode(b'YmluYXJ5AHgwMHN0cmluZw=='))
print('\n')

b64e = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b64e)
b64ue = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b64ue)
b64ud = base64.urlsafe_b64decode(b'abcd--__')
print(b64ud)


s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)