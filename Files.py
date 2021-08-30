# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:42:39 2021

@author: turgu
"""

# with open('pi.txt') as fayl:
#     pi=fayl.read()
# pi=pi.rstrip()
# pi=pi.replace('\n','')
# print(pi)
# with open('my.txt') as fiile:
    
#     for line in fiile:
#         print(line)
        
# with open('my.txt') as fayll:
#     students = fayll.readlines()
# students = [student.rstrip() for student in students]
# print(students)

# falename ='33-lesson'
# with open(falename,'w') as fayl:
#     fayl.write('I am working on 33-lesson')
# print(fayl)


# filename='new_topic'
# age=18
# name='Nurmuhammad'
# with open(filename,'w') as fayl:
#     fayl.write(str(age))
#     fayl.write(name)
# print()


# import pickle
# talaba1 ={'hasan':'tatu','olim':'samtuit','nazik':'jahon tillar'}
# with open('info','wb') as file:
#     pickle.dump(talaba1,file)
# with open('info','rb') as file:
#     talaba1 =pickle.load(file)
# print(talaba1)

with open('pi_million_digits.txt') as file:
     pi=file.read()
pi =pi.rstrip()
pi =pi.replace('\n','')
 
bday='242021'
print(bday in pi) 













