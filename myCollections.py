#-*- coding: utf-8 -*-
# myCollections.py
# @author John Doe
# @description 
# @created Tue Oct 30 2018 16:18:12 GMT+0800 (CST)
# @last-modified Fri Nov 02 2018 11:19:51 GMT+0800 (CST)
#

from collections import namedtuple, deque, defaultdict
from collections import OrderedDict

point = namedtuple('Point', ['x', 'y'])
p = point(1, 2)
print(p.x, p.y)

print(isinstance(p, point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])

# 双端队列 deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# ChainMap 
# 本身也是一个dict，但是查找的时候，
# 会按照顺序在内部的dict依次查找。

from collections import ChainMap
import os, argparse

# structure parameter
defaults = {
    'color': 'red',
    'user': 'guest'
}

# structure cmd parameter
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k:v for k, v in vars(namespace).items() if v}

# combine ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)
print('color = %s' % combined['color'])
print('user = %s' % combined['user'])


# Counter
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)

