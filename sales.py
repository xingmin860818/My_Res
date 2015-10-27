#!/usr/bin/env python
''' 
Used to show the price of the same goods,at different
festival
'''
def weekday_deco(func):
        def wrapper(**kw):
                try:
                        func(**kw)
                        d = {x:kw[x]*0.9 for x in kw}
                        return d
                except TypeError:
                        raise TypeError(r'you should input argument like this: a=100')
        return wrapper
def duble_eleven_deco(func):
        def wrapper(**kw):
                try:
                        func(**kw)
                        d = {x:kw[x]*0.8 for x in kw}
                        return d
                except TypeError:
                        raise TypeError(r'you should input argument like this: a=100')
        return wrapper



@weekday_deco
@duble_eleven_deco
def set_price(**kw):
        return kw

#print set_price(Iphone=5000,NIKE=600,ThinkPad=5500)
#{'NIKE': 540.0, 'Iphone': 4500.0, 'ThinkPad': 4950.0}
