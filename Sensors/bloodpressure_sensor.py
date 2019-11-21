import time
import random
import json
import sys
import Sender.sender as sdr

import threading
from Sensors.sensor import Sensor
from Const.config import PORT

class BpSensor(Sensor):
    def __init__(self, power, duty_cycle, data, message_topic, frequency_of_message):
        Sensor.__init__(self, power, duty_cycle, data, message_topic, frequency_of_message)

    def sensor_data(self):
        record_data = {'sid': self.message_topic, 'timestamp': time.ctime(time.time()), 'systolic': random.randint(120, 180),
                       'diastolic': random.randint(80,130),
                       'battery': self.power
                       }
        if(record_data['systolic'] >180 or record_data['diastolic'] > 120):
            record_data['alert'] = 'Hypertensive Crisis - Seek Medical Care'
        elif(record_data['systolic'] >= 140 or record_data['diastolic'] >= 90):
            record_data['alert'] = 'High Blood Pressure (Hypertension Stage 2'
        elif ((record_data['systolic'] >= 130 and record_data['diastolic'] <= 139) or
                  ((record_data['diastolic'] >= 80 and record_data['diastolic'] <= 89))):
            record_data['alert'] = 'High Blood Pressure (Hypertension Stage 1)'
        elif(record_data['systolic'] >= 120 and record_data['systolic'] <= 129 and record_data['diastolic'] < 80):
            record_data['alert'] = 'Blood Pressure Elevated'



        record = json.dumps(record_data)
        print("BP level data generated")
        print("Data:", record)
        return record

    def send_data(self):
        self.data = self.sensor_data()
        # send data
        sdr.send(self.data, PORT)
        self.power = self.battery.decrease_trans_energy(sys.getsizeof(self.data))
        print("size: ", sys.getsizeof(self.data))
        print("energy level: ", self.power)