# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:29:12 2021

@author: turgu
"""
turnik = int(input('nechta tortinding?>'))
if turnik < 0:
    print('manfiy son kiritish mumkin emas')
elif turnik == 0:
    print('ha ahmoq,tortinolmadingmi')

elif turnik <= 5:
    print('yahshi')
elif turnik <=8:
    print('o gap yoo')
elif turnik <=15:
    print('buriev bopketbsanu')

else:
    print('shvarsnegir') 