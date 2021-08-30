# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 20:34:29 2021

@author: Bozoroff #31-lesson/Incapsulation
"""
from uuid import uuid4
class Auto:
    """Automobil's class """
    num_auto = 0
    def __init__(self,make,model,colour,year,cost,km=0):
        """Automobil's feature"""
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.cost = cost
        self.__km = km
        self.__id = uuid4()
        Auto.num_auto +=1
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    def add_km(self,km):
        """Add another mile to the mileage of the car"""
        if km>=0:
            self.__km += km
        else:
            print("we can't reduce the km of the car")
    @classmethod
    def get_num_avto(cls):
        return cls.__num_auto
auto1 = Auto("GM","Malibu","Qora",2020,40000,1000)
print(f"ID: {auto1.get_id()}")
auto1.add_km(1500)
print(auto1.get_km())

auto1 = Auto("GM","Malibu","Qora",2020,40000)
auto2 = Auto("GM","Lacetti","Oq",2020,20000)
print(auto1.num_auto)








