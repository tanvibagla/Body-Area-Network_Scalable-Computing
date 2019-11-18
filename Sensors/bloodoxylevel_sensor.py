import time
import random
import json
import sys
import Sender.sender as sdr

import threading
from Sensors.sensor import Sensor
from Const.config import OXYLEVEL_PORT

class OxySensor(Sensor):
    def __init__(self, power, duty_cycle, data, message_topic, frequency_of_message):
        Sensor.__init__(self, power, duty_cycle, data, message_topic, frequency_of_message)

    def sensor_data(self):
        record_data = {'sid': self.message_topic, 'timestamp': time.ctime(time.time()), 'oxygen': random.randint(80, 100)}
        record = json.dumps(record_data)
        print("Oxygen level data generated")
        print("Data:", record)
        return record

    def send_data(self):
        self.data = self.sensor_data()
        # send data
        sdr.send(self.data, OXYLEVEL_PORT)
        self.power = self.battery.decrease_trans_energy(sys.getsizeof(self.data))
        print("size: ", sys.getsizeof(self.data))
        print("energy level: ", self.power)