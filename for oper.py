# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 23:53:38 2021

@author: turgu
"""

ismlar = ['vali','ali','salim','nodir','farrux']
for ism in ismlar:
    print(f"{ism}, uyingga ertaroq bor \nonang kutvotti \n")

sonlar = list(range(11,101,2))
for son in sonlar:
    print(f"{son**3} \n")
#
n_people = int(input("bugun necha kishi bn uchrashdingiz")) 
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-uchrashgan insoninggiz kim edi:"))
print(ismlar)    
   