# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:34:05 2021

@author: turgu
"""
book = input('qaysi kitob kerak?>>>>')
if book == 'inferno':
    print('ha bizda bu kitob bor')
else:
    print('uzr bizda bu kitob yooo')
    #login
login = input('loginni kiriting')
if login == 'admin':
    print('hush kelibsiz admin.\nfoydalanuvchi royhatini korasizmi?')
else:
    print(f"xush kelibsiz {login}")
#2ta son
a = int(input('1-sonni kiriting'))
b = int(input('2-sonni kiriting'))
if a == b:
    print('sonlar teng')
else:
    print('teng emasaa')
son = float(input('istalgan son kiriting'))
 
if son > 0:
    print(son**(1/2))
else:
    print('musbat son kiriting33')
    
    
    
    