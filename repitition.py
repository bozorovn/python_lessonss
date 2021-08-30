# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 10:47:56 2021

@author: Bozoroff
"""

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#     def tanishtir(self):
#         return f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman"

# talaba1 = Talaba("Alijon","Valiyev",2000)

# class User:
#     def __int__(self,name,username,email):
#         self.name = name
#         self.uname = username
#         self.mail = email
    
#     def describe():
#         pass
    
#     def get_email():
#         pass


class Foydalanuvchi:
    def __init__(self,name,surname,username,email):
        self.name=name
        self.surname=surname
        self.username=username
        self.email=email

Foy1 = Foydalanuvchi('Ali','Nazimov','Nurchik','nurchikbozorov@gmail.com')    