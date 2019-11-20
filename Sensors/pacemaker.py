import time
import random
import json
import sys
import Sender.sender as sdr

import threading
from Sensors.sensor import Sensor
from Const.config import PORT

class Pacemaker(Sensor):
    def __init__(self, power, duty_cycle, data, message_topic, frequency_of_message):
        Sensor.__init__(self, power, duty_cycle, data, message_topic, frequency_of_message)

    def sensor_data(self):
        record_data = {'sid': self.message_topic, 'timestamp': [], 'bpm': None, 'battery': self.power}
        # record_data['sid'] = 'Heart Rate'
        record_data['timestamp'] = time.ctime(time.time())
        record_data['bpm'] = random.randint(65, 100)
        record = json.dumps(record_data)
        print("Pacemaker data generated")
        print("Data:", record)
        return record

    def send_data(self):
        self.data = self.sensor_data()
        # send data
        sdr.send(self.data, PORT)
        self.power = self.battery.decrease_trans_energy(sys.getsizeof(self.data))
        print("size: ", sys.getsizeof(self.data))
        print("energy level: ", self.power)

