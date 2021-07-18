# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:41:07 2021

@author: turgu
"""

import phonenumbers
from phonenumbers import geocoder
phone_number = phonenumbers.parse("+998900120525")
print(geocoder.description_for_number(phone_number,'en'))
print(phonenumbers)