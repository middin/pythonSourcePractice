# -*- coding: utf-8 -*-
# myPickle.py
# @author John Doe
# @description 
# @created Mon Oct 29 2018 14:10:20 GMT+0800 (CST)
# @last-modified Mon Oct 29 2018 14:18:58 GMT+0800 (CST)
#

import pickle

f = open('dump.txt', 'wb')
d = dict(name = 'Bob', age = 20, score = 80)
pickle.dump(d, f)
f.close()

f1 = open('dump.txt', 'rb')
d1 = pickle.load(f1)
f1.close()
print(d1)