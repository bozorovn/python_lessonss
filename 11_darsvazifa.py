# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 19:28:27 2021

@author: turgu
"""
#cafeda
ovqatlar = ['osh','lagmon','xonim','chuchvara','shashlik','lavash','gamburger','somsa']
mijoz_royhati = []
for n in range(4):
    mijoz_royhati.append(input(f'{n+1}-ovqat>>>'))
bor_ovqatlar = []
yoq_ovqatlar = []
for ovqat in mijoz_royhati:
    if ovqat in ovqatlar:
        bor_ovqatlar.append(ovqat)
    else:
        yoq_ovqatlar.append(ovqat)
if bor_ovqatlar:
    print('kafeyimizda mana bu ovqatlar bor:')
    for ovqat in bor_ovqatlar:
     print(ovqat)
else:
        print('bizda siz soragan hamma ovqatlar bor ')
  ##################      
        
        
        
        
        
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

################

mahsulotlar = ['kartoshka','lampa','guruch','grichka','priprava','tuz','zelen','tuxum''banan',
               'apelsin','shakar']
bor_mahsulotlar = [ ]
mavjud_emas = []
for n in range(5):
    bor_mahsulotlar.append(input(f'savatga {n+1}- mahsulotni qoshing>>'))

if bor_mahsulotlar:
    for mahsulot in bor_mahsulotlar:
        if mahsulot in mahsulotlar:
            print(f'dokonimizda {mahsulot} bor')
        else:
            print(f'dokonimizda {mahsulot} yooo')            
       





















        