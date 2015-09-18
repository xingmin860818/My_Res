#!/usr/bin/env python
#-*-coding:utf-8-*-
#定义成绩单类
class chengjidan(object):
	def __init__(self,banjiname):
		self.banjiname = banjiname
		self.students = [] #定义学生实例列表
	def add(self,student):
		self.students.append(student) #添加学生类实例到列表
	#取最高分方法
	def max_score(self,kemu):
		max_f = 0
		person = ''
		for stu in self.students:
			chengji = stu.getscore(kemu)
			if chengji > max_f:
				max_f = chengji
				person = stu.name
		return '科目：%s\t最高分：%s\t姓名：%s' % (kemu,max_f,person)
	#取平均分方法
	def average_score(self,kemu):
		scores = []
		for stu in self.students:
			chengji = stu.getscore(kemu)
			scores.append(chengji)
		total_f = 0
		for score in scores:
			total_f += score
		average_f = total_f / len(scores)
		return '所选科目与：%s\t平均分：%s' % (kemu,average_f)
	#取学员各科总成绩方法
	def total(self):
		for stu in self.students:
			person = ''
			total_f = 0
			for kemu in  stu.total_score():
				person = stu.name
				total_f += stu.total_score()[kemu]
			print '姓名：%s\t总分：%s' % (person,total_f)
#定义学员类
class student(object):
	def __init__(self,name):
		self.name = name
		self.kemus = {}
	#学员学习时科目分数置0
	def study(self,kemu):
		self.kemus[kemu] = 0
	#学员考试成绩录入方法
	def kaoshi(self,kemu,score):
		self.kemus[kemu] = score
	#取科目成绩方法
	def getscore(self,kemu):
		return self.kemus[kemu]
	#取
	def total_score(self):
		return self.kemus
tom = student('Tom')
jerry = student('Jerry')
c = chengjidan('07351')
c.add(tom)
tom.kaoshi('wuli',90)
tom.kaoshi('huaxue',92)
tom.kaoshi('shuxue',84)
c.add(jerry)
jerry.kaoshi('wuli',60)
jerry.kaoshi('huaxue',94)
jerry.kaoshi('shuxue',84)
print c.max_score('wuli')
print c.average_score('huaxue')
c.total()
