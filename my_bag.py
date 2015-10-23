#!/usr/bin/env python
#-*-coding:utf8-*-

class BackPack(object):
        def __init__(self):
                #初始化物品存放字典
                self.stuff_dic = {}
                #初始化包的最大容量
                self.max_size = 100
                #初始化包内0物品值
                self.stuffs_size = 0
        #查看包内物品
        def show_stuffs(self):
                return self.stuff_dic
        #查看保内剩余空间
        def show_free_space(self):
                return(self.max_size - self.stuffs_size)
        #向包内存放物品，有名称，数量和大小
        def add_stuff(self,stuff,num,size):
                try:
                        #根据物品数量乘以大小向包内存放，如果最大量存不下就减少一个，知道能存下为止
                        for i in range(1,num+1)[::-1]:
                                if self.stuffs_size + i*size <= self.max_size:
                                        self.stuff_dic[stuff] = [i,i*size]
                                        self.stuffs_size += i*size
                                        return 'you can only put %s\'s %s in it' % (i,stuff)
                                else:
                                        continue
                except TypeError,e:
                        raise
        #从包内去物品
        def get_stuff(self,stuff,num):
                try:
                        #根据输入的物品名称从字典中查找匹配物品
                        for k in self.stuff_dic:
                                if k == stuff:
                                        #找到相应物品，取出输入数量，字典内相应减少数量和增加剩余空间
                                        x = self.stuff_dic[k]
                                        self.stuffs_size -= num*(x[1]/x[0])
                                        x[1] -= num*(x[1]/x[0])
                                        x[0] -= num
                                        if x[0] == 0:
                                                self.stuff_dic.pop(stuff)
                                                break
                except TypeError:
                        raise
