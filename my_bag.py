#!/usr/bin/env python

class BackPack(object):
	def __init__(self):
		self.bag_list = []
		self.total_size = 0
	def list_stuffs(self):
		return self.bag_list,self.total_size
	def add_stuffs(self,stuffs,size):
		self.stuff_dic = {}
		self.total_size += size	
		if self.total_size > 70:
			return('Bag is full,cannot put %s in the bag' % self.total_size)
		self.stuff_dic[stuffs] = size
		self.bag_list.append(self.stuff_dic)
	def get_stuffs(self,stuffs):
		for i in self.bag_list:
			for k in i:
				if k == stuffs:
					self.bag_list.pop(self.bag_list.index(i))
					self.total_size -= i[k]
					break

b = BackPack()
b.add_stuffs('apple',30)
b.add_stuffs('apple',20)
b.add_stuffs('pair',20)
b.get_stuffs('apple')
print b.list_stuffs()
