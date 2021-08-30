# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:01:12 2021

@author: Bozoroff
"""
 
    
    
class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    
    def get_name(self):
        """Fan nomi"""
        return self.nomi
    
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [x.get_info() for x in self.talabalar]
    
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni
     
