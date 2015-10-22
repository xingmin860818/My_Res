#!/usr/bin/env python
#-*-coding:utf8-*-

class BackPack(object):
	def __init__(self):
		#定义包中物品列表
		self.bag_list = []
		#定义空包物品的初始值
		self.total_size = 0
	def list_stuffs(self):
		#查看包内物品和占用量
		return self.bag_list,self.total_size
	def add_stuffs(self,stuffs,size):
		#定义存放物品，需要输入物品名称和对应占空间量
		self.stuff_dic = {}
		#包的最大容量是70L，如果存放物品累加达到这个值就会提示错误,并且实时返回剩余空间
        	if (self.total_size+size) <= 70:
                	print 'you can put less than %s things in it' % (70 - self.total_size)
			self.stuff_dic[stuffs] = size
        		self.total_size += size
			self.bag_list.append(self.stuff_dic)
		else:
			print 'Bag is full,cannot put %s in it' % stuffs
	def get_stuffs(self,stuffs):
		#取物品，匹配到多个相同物品，只从中取一个
		for i in self.bag_list:
			for k in i:
				if k == stuffs:
					self.bag_list.pop(self.bag_list.index(i))
					self.total_size -= i[k]
					break

b = BackPack()
b.add_stuffs('apple',30)
b.add_stuffs('apple',20)
b.add_stuffs('pair',10)
b.add_stuffs('banana',30)
print b.list_stuffs()
b.get_stuffs('apple')
print b.list_stuffs()
