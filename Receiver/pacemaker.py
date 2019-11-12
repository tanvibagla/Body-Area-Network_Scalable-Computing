# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:53:05 2019

@author: Yeshwanth

"""

import json
import time
import random

class pacemaker:
    def __init__(self, power, duty_cycle, data, message_topic, frequency_of_message):
        self.power = power
        self.duty_cycle = duty_cycle
        self.data = data
        self.message_topic = message_topic
        self.frequency_of_message = frequency_of_message

    def pacemaker_data(self, record):
        record_data = {'sid':'Heart Rate','timestamp':[],'bpm':None}
        i=0
        with open('sensor.json','a',encoding='utf-8') as fjson:
            while True:
                record_data['sid'] = 'Heart Rate'
                record_data['timestamp'] = time.ctime(time.time())
                record_data['bpm'] = random.randint(65,100)
                i += 1
                record = json.dumps(record_data)
                if i == 100:
                    break
                fjson.write('{}\n'.format(record))
            fjson.close()    


if __name__ == '__main__':
    pm = pacemaker(100, 20, {}, 'Pacemaker Data', 3)
    pm.pacemaker_data(pm.data)

'''
with open('sensor.json','a',encoding='utf-8') as f:
    json.dump([],f)
    
#feeds = []
'''
# with open('sensor.json','a',encoding='utf-8') as fjson:
#     a = json.dumps(d)
#     #feeds.append(d)
#     fjson.write('{}\n'.format(a))