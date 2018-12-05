#-*- coding: utf-8 -*-
# myStruct.py
# @author John Doe
# @description 
# @created Sat Nov 10 2018 14:19:42 GMT+0800 (CST)
# @last-modified Tue Nov 13 2018 11:00:24 GMT+0800 (CST)
#

import struct

# '>' big-endian 'I' 4字节无符号整数
sp = struct.pack('>I', 10240099)
print(sp)

# unpack requires a buffer of 6 bytes
sup = struct.unpack(">IH", b'\xf0\xf0\xf0\xf0\x80\x80')
print(sup)