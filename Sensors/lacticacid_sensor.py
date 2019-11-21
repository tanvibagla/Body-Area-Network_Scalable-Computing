import time
import random
import json
import sys
import Sender.sender as sdr

import threading
from Sensors.sensor import Sensor
from Const.config import PORT, PORT_SINK_2


class LacticSensor(Sensor):
    def __init__(self, power, duty_cycle, data, message_topic, frequency_of_message):
        Sensor.__init__(self, power, duty_cycle, data, message_topic, frequency_of_message)

    def sensor_data(self):
        record_data = {'sid': self.message_topic, 'timestamp': time.ctime(time.time()), 'lacticlevel': random.randint(80, 100),
                       'battery': self.power
                       }
        record = json.dumps(record_data)
        print("Lactic level data generated")
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