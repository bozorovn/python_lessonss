# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 14:22:13 2021

@author: Bozoroff
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
inson = Shaxs("Hasan","Alimov","FB001122",1995)
print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")


class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
talaba = Talaba("Valijon","Aliyev","FA112299",2000,4122331,'abdulla qahhor kocha')
print(talaba.get_info())
    
    

    
























class Car():
    def __init__(self,name,colour,year):
        self.name=name
        self.colour=colour
        self.year=year
    def get_info(self):
        info = f"The name of the car: {self.name}, colour:{self.colour},"
        info += f"year:{self.year}"
        return info
    def get_name(self):
        return self.name
    def get_colour(self):
        return self.colour
    def get_year(self):
        return self.year
    
car_1 = Car('camaro','red',2021) 
print(car_1.get_info())   
    
    
    
    
    