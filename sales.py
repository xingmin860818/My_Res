#!/usr/bin/env python
#-*-coding:utf8-*-
''' 
Used to show the price of the same goods,at different
festival
'''
#####周末打8折######
def weekend(func):
        def wrapper(price):
                discount = 0.8
                return func(price)*discount
        return wrapper
#####双11打8折#####
def double_eleven(func):
        def wrapper(price):
                discount = 0.8
                return func(price)*discount
        return wrapper

#####打折叠加#####
@weekend
@double_eleven
def price(price):
        return price

#####商品定价####
def goods_price(**kw):
        dic = {}
        for k,v in kw.iteritems():
                dic[k] = '%.2f' % price(v)
        return dic

