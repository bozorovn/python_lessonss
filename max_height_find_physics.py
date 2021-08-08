# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:51:16 2021

@author: turgu
"""

v0=int(input('boshlangich tezlikni kiriting:'))
t=int(input('vaqtni kiritning:'))
g=9.8
qan_har = input("qandey harakat : yuqoriga(1) yoki pastga(2)?")
if qan_har == '1':
    print(f'jism kotariladigon maksimal balandlik {v0*t-g*t**2} ga teng')
elif qan_har == "2":
    print( f'jism kotariladigon maksimal balandlik {v0*t+g*t**2} ga teng')