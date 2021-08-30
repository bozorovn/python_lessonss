# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 22:34:10 2021

@author: Bozoroff
"""
# ##restoran_proect
# print('Assalom alaykum, restoranimizga xush kelibsiz!')

# bor_ovqatlar=['kabob','palov','somsa','china salad']
# buyurtmalar = []

# print(f"bizda shu {bor_ovqatlar} ovqatlar bor ")
# buyurtma = input('Nima buyurasiz? >>')
# if buyurtma in bor_ovqatlar:
#     buyurtmalar.append(buyurtma)
#     print(f'buyurtma qabul qilindi.\nsiz buyurgan buyurtmalar {buyurtmalar}')
     
# else:
#     print('ovqat nomini togri yozing.')
 
# import math

# print('kv tenglama ishlab beraman, ax^2+bx+c=0')
# a = 1
# b = -5
# c = 6
# D = b**2 - 4*a*c
# print(f'D={D}')
# print(f"2*a={2*a}")
# if D > 0:
#     x1 = (-b + math.sqrt(D) )/2*a
#     x2 = (-b - math.sqrt(D) )/2*a
#     print(f'x1={x1}, x2={x2}')
# elif D == 0:
#     x = (-b) / 2 * a
#     print(f'bitta yechim:{x}')
# else:
#     print('Xning butun qiymatlari yo')
    
# talaba_1 = {}
# talaba_1['ism'] = 'Sardor Nuriddinov'
# talaba_1['kurs'] = 2
# talaba_1['yosh'] = 19
# # print(talaba_1)
# print(f"Talaba: {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")  

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# phone = telefonlar.get('hasan','Bunday ism mavjud emas')
# # print(telefonlar)
# print()


# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz

# son = 1
# while son<=5:
#     print(son, end=' ')
#     son+=1

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")


son = 0
while son<10:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son, end=' ')
        











    
    