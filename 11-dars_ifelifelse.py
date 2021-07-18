# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:15:20 2021

@author: turgu
"""
                                #mustaqil ishlar
#kafeda buyurtma
menu = ['somsa','manti','kabob','jigar','shorva']
ovqat = input('nima ovqat yeysiz?')
if ovqat.lower() in menu:
    print('buyurtma qabul qilindi')
else:
    print('afsuski bizda bundey ovqat yoo')

menu = ['somsa','manti','kabob','jigar','norin']
buyurtmalar = ['dimlama','somsa','jigar','palov']

for taom in buyurtmalar:
    if taom in menu:
        print(f'menuda {taom} bor')
    else:
        print(f'kechirasiz, menuda {taom} yoo')






#zooparkga kirish
yosh = int(input('yoshinggiz nechida>>>'))
if yosh<=4:
   narx = 0
elif yosh<=18:
   narx = 5000  
elif yosh<=30:
    narx = 8000
else:
    narx = 10000
print(f'sizga kirish {narx} som')    
 










#hafta kuni
kun = input('bugun qaysi kun?>')
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('bugun dam olish kuni')
else:
    print('bugun ish kuni')
kun = input('bugun qandey kun') 
temp = float(input('bugun harorat qande'))
if kun.lower() == 'chorshanba' and temp >= 30:
   print('bugun ovqat qilaman')
elif kun.lower()=='chorshanba' and temp < 30:
       print('ovqat qimiman')
else:
    print('hich nima')    
#non choy    
narx = 15000
choy = 1
non = 0
if choy and non:
    narx = narx + 10_000
elif choy or non:
    narx = narx +5_000
    
print(f'jami {narx} som')    
    
    
 #turnkda tortininsh   
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
    
    
    
                                #########vazifalar
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
            
    
 #4-topshiriq

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
       #5-topshiriq
       

foydalanuvchilar = ['Nurbek','sardor','hayotbahrom','Nurmuhammad','asadbek']
login = input('loginni kiriting>>')
if login in foydalanuvchilar:
    print('login band yangi login kiriting')
else:
    print('welcome')
    

#6-topshiriq

ison = int(input('istalgan butun son kiriting>>'))
for n in  range(2,11):
    if  (ison%n):
        print(f'{ison} soni {n} ga qoldqli bolinadi')    
    
    
    
    
    
    
    
    