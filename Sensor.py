# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:53:05 2019

@author: Yeshwanth

"""

import json
import time
import random

d = {'sid':'Heart Rate','timestamp':[],'bpm':None}
a = list(d.keys())
for i in range(1):
    d[a[i]] = a[i]
    d[a[i+1]] = time.ctime(time.time())
    d[a[i+2]] = random.randint(65,100) 
'''
with open('sensor.json','a',encoding='utf-8') as f:
    json.dump([],f)
    
#feeds = []
'''
with open('sensor.json','a',encoding='utf-8') as fjson:
    a = json.dumps(d)
    #feeds.append(d)
    fjson.write('{}\n'.format(a))