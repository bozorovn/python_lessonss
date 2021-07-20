# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 10:10:48 2021

@author: Bozoroff

"""
#functions:moduls
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting",end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")    
        #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
        #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")
    
    
    ##Python moduls
import math
x=int(input('son kiriting:'))
print(math.sqrt(x))   
#
x=int(input('sonni kiriting:'))
y=int(input('qaysi darajaga oshirmoqchisiz:'))
print(math.pow(x,y))
# 
print(math.pi)

import random as r
son = r.randint(10,100)
print(son)
names = ['ali','vali','Nurmuhammad','nodir','giwmat','towmat','gani','vali','wamsi'
          'ahmad','wahmat','mamareyim','olim']
name = r.choice(names)
print(name)
print(r.choice(name))

x=list(range(0,99,3))
print(x)
print(f"shulardan tasodifiy son:{r.choice(x)}")


x=list(range(12))
print(x)
r.shuffle(x)
print(x)
 


