# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:50:09 2021

@author: Bozoroff
"""

#Linear_search

# def linear_search(list, item):
#    for n in range(len(list)):
#        if list[n]==item:
#             return n
#    return None
# print(linear_search([1,3,5,6,34,56], 6))

# def linear_search1(list,t):
#     for n in range(len(list)):
#         if list[n]==t:
#             return n
#     return None
# print(linear_search1(range(1,45),6))

#Binary search
def binary_search(list,item):
    low=0
    high=len(list)-1
    while low<=high:
        middle=(low+high)//2
        guess=list[middle]
        if guess==item:
            return middle
        if guess>item:
            high=middle-1
        else:
            low=middle+1
    return None
print(binary_search([1,2,33,44,55,55,55,34,56],55))
    