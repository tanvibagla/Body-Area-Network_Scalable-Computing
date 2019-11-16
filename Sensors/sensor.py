import time
import logging

from Energy import Battery
from Const.config import DECAY_RATE, DECAY_WHILE_DATA_TRANSFER


class Sensor:
    def __init__(self, power, duty_cycle, data, message_topic, frequency_of_message):
        self.power = power
        self.duty_cycle = duty_cycle
        self.data = data
        self.message_topic = message_topic
        self.frequency_of_message = frequency_of_message
        self.battery = Battery(sensor_type='H')

    def sensor_data(self, record):
        self.battery.decrease_trans_energy()
        pass

    def power_decay(self, data_size):
        # self.power = self.battery.decrease_trans_energy(data_size)
        print("Power decay calculated")
        return self.power

    def send_data(self, record):
        self.sensor_data(record)
        self.power = self.power_decay() - DECAY_WHILE_DATA_TRANSFER * self.power

    def send_data(self):
        pass

    def charging(self):
        pass



