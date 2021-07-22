# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 14:24:25 2021

@author:Bozoroff
"""
#lambda_function
import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

yuza = lambda pi, r : pi*r**2
# print(yuza(math.pi,2))

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")



sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(math.sqrt,sonlar))
# print(ildizlar)

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x
print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz

kvadratlar = list(map(lambda x:x*x,sonlar))
# print(kvadratlar)

ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.title(),ismlar)))
###
import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

# print(sonlar)
# print(juft_sonlar)

x = int(input('Enter a number:'))

print((lambda x: x**4)(x))


















