# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:49:50 2021

@author: Bozoroff
"""

def sumnum(a,b):
    summa=a+b
    return summa
def maxthree(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
print(maxthree(3,4,5))
ex_list=[3,23,34,44]
print(min(ex_list))   
def factorial(N):
    i=1
    fact=1
    while i!=N+1:
        fact=fact*i
        i+=1
    return fact
print(factorial(5))
 