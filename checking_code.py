#!/usr/bin/env python
#-*-coding:utf8-*-
import random
import string

def gener_list():
        #生成一个包含大写，小写字母和数字的列表
        L = []
        #将ASCII码转换为对应字母和符号
        chars = map(chr,range(65,123))
        for words in chars:
                #通过isalpha函数过滤掉非字母字符
                if words.isalpha():
                        L.append(words)
        for num in range(0,2):
                L.append(str(num))
        return L


#定义函数,生成任意长度随机数
def gener_random(n):
	if n == 0:
		return ""
	else:
		x = random.choice(gener_list())
		#递归生成n位随机数
		rand_num = x + str(gener_random(n-1)) 
		return rand_num

if __name__ == '__main__':
	check_list = []
	while 1:
		input_num = raw_input('How many Random words do you wangt?::').strip()
		try:
			number = int(input_num)
			x = gener_random(number)
			if x  in check_list:
				print 'Warning: this check-code has already in used,please try again'
			else:
				check_list.append(x)
				print '\033[32;1m%s\033[0m' % x #此处如果生成一个满足条件可以加上break
		except ValueError,e:
			print('\033[31;1mPlease input an integer!\nexcept:%s\033[0m') % e
