# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:47:07 2019

@author: tanvi
"""

import json
import time
import random
 
d = {'diastolic':None,'systolic':None,'sid':'Blood Pressure','timestamp':[]}
a = list(d)
print d
i=0
with open('sensor.json','a') as fjson:
 for i in range(10):
      #d['sid'] = a[i]
      d['timestamp'] = time.ctime(time.time())
      d['systolic'] = random.randint(80,120)
      d['diastolic'] = random.randint(60,80) 
      a = json.dumps(d)
      #feeds.append(d)
      fjson.write('{}\n'.format(a))
fjson.close()
#'''
#with open('sensor.json','a',encoding='utf-8') as f:
#    json.dump([],f)
#    
##feeds = []
#'''
#with open('sensor.json','a',encoding='utf-8') as fjson:
#    a = json.dumps(d)
#    #feeds.append(d)
#    fjson.write('{}\n'.format(a))

