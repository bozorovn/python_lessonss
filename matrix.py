# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:10:58 2021

@author: Bozoroff
"""
from numpy import * 
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
m = reshape(a,(7,5))
# print(m)
 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
    
# Print data for Wednesday
# print(m[2])

# # Print data for friday evening
# print(m[4][3])
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
m_r = append(m,[['Avg',12,15,13,11]],0)

print(m_r)
