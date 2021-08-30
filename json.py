# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:14:59 2021

@author: Bozoroff
"""
import json
Tesla ={'yili':'2021',
        
        'model':'chotkiy',
        'colour':'blue'}
Tesla_json=json.dumps(Tesla)
with open("Tesla.json","w") as f:
    json.dump(Tesla,f)
    
Tesla=json.loads(Tesla_json)