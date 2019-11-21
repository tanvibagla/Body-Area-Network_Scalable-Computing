import time
import random
import json
import sys
import Sender.sender as sdr

import threading
from Sensors.sensor import Sensor
from Const.config import PORT, PORT_SINK_2

class Pacemaker(Sensor):
    def __init__(self, power, duty_cycle, data, message_topic, frequency_of_message):
        Sensor.__init__(self, power, duty_cycle, data, message_topic, frequency_of_message)

    def sensor_data(self):
        record_data = {'sid': self.message_topic, 'timestamp': [], 'bpm': None, 'battery': self.power}
        # record_data['sid'] = 'Heart Rate'
        record_data['timestamp'] = time.ctime(time.time())
        record_data['bpm'] = random.randint(50, 150)
        if(record_data['bpm'] < 60 or record_data['bpm'] > 100):
            record_data['alert'] = 'Heart Rate is not normal. Inform Doctor'
        record = json.dumps(record_data)
        print("Pacemaker data generated")
        print("Data:", record)
        return record

    def send_data(self):
        try:
            self.data = self.sensor_data()
            # send data
            sdr.send(self.data, PORT)
            self.power = self.battery.decrease_trans_energy(sys.getsizeof(self.data))
            print("size: ", sys.getsizeof(self.data))
            print("energy level: ", self.power)
        except:
            print("Server not available")
            self.data = self.sensor_data()
            # send data
            sdr.send(self.data, PORT_SINK_2)
            self.power = self.battery.decrease_trans_energy(sys.getsizeof(self.data))
            print("size: ", sys.getsizeof(self.data))
            print("energy level: ", self.power)

