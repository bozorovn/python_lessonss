# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:59:52 2021

@author: turgu
"""

import psutil
battery =psutil.sensors_battery()
percent= int(battery.percent)
print(f"qurilmangiz zaryadi: {percent}%")
