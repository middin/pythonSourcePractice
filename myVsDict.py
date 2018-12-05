# -*- coding: utf-8 -*-
# myVsDict.py
# @author John Doe
# @description 
# @created Sat Oct 27 2018 17:01:51 GMT+0800 (CST)
# @last-modified Sat Oct 27 2018 17:02:14 GMT+0800 (CST)
#

class Dict(dict):
	"""dict"""
	def __init__(self, **kw):
		super().__init__(**kw)
	
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribue '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value
