#!/usr/bin/env python
#-*-coding:utf8-*-
import os
import time
#列出目录中所有的文件绝对路径，保存到列表中
filelis = []
def listdir(dir):
	lis = os.listdir(dir)
	path = os.path.abspath(dir)
	for file in lis:
		abspath = os.path.join(path,file)
		if os.path.isdir(abspath):
			listdir(abspath)

		else:
			filelis.append(abspath)
	return filelis

#给所有文件组合上修改时间和占空间大小
def get_mtime_size(listdir):
	for i in listdir:
		mtime = time.ctime(os.path.getmtime(i))
		#提取文件的大小，'/1024表示转换计量单位'
		filesize = (os.path.getsize(i)/1024/1024)
		print ('%s\t%sM\t%s') % (mtime,filesize,i)
