# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:32:34 2021

@author: turgu
"""

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
       