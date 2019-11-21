import time
import logging
import sys
import Sender.sender as sdr

from Energy import Battery
from Const.config import PORT, PORT_SINK_2


class Sensor:
    def __init__(self, power, duty_cycle, data, message_topic, frequency_of_message):
        self.power = power
        self.duty_cycle = duty_cycle
        self.data = data
        self.message_topic = message_topic
        self.frequency_of_message = frequency_of_message
        self.battery = Battery(sensor_type='H')

    def sensor_data(self, record):
        pass

    def power_decay(self, data_size):
        # self.power = self.battery.decrease_trans_energy(data_size)
        print("Power decay calculated")
        return self.power

    def send_data(self, record):
        self.sensor_data(record)
        # self.power = self.power_decay() - DECAY_WHILE_DATA_TRANSFER * self.power

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

    def battery_decay_while_idle(self):
        self.power = self.battery.decrease_energy()

    def charging(self):
        pass



