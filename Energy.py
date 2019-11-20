# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:16:50 2019

@author: yesh2
"""

Power_Type={0:'Charging',1:'On Battery',2:'Dead'}

class Battery(object):
    P_TX = 0.084  # Watts
    P_RX = 0.073  # Watts

    E_INIT = 0.49  # Joules
    E_MIN = 0.5   # Joules  to operate

    # charging  rate
    P_CHARGING = 0.005  # Watts

    # idle discharge rate
    P_IDLE = 0.001  # Watts

    # transmission rate
    TR_RATE = 250   # kbps
    
    def __init__(self,sensor_type,power_type=1,**kwargs):
        self.type = sensor_type or 'H'
        self.power_type = power_type
        self.energy_consume = 0
        self.energy = self.E_INIT
        
    
    def decrease_trans_energy(self, packet_size):
        # power consumption = Tx power * Tx time
        tx_time = (packet_size * 8.0 / self.TR_RATE / 1024.0)
        energy_dec = self.P_TX * tx_time
        if self.power_type != 0:
            self.energy -= energy_dec
        self.energy_consume += energy_dec
        return self.energy
    
    def decrease_receive_energy(self, packet_size):
        # power consumption = Rx power * Tx time
        tx_time = (packet_size * 8.0 / self.TR_RATE / 1024.0)
        energy_dec = self.P_RX * tx_time
        if self.power_type != 0:
            self.energy -= energy_dec
        # self.energy_consume += energy_dec
        
        return self.energy
    
    def decrease_energy(self, discharging_rate=None, discharging_time=1):
        energy_dec = (discharging_rate or self.P_IDLE) * discharging_time
        if self.power_type != 0:
            self.energy -= energy_dec
        self.energy_consume += energy_dec
        return self.energy

    def have_energy(self):
        if self.energy > self.E_MIN:
            print('Has battery')
            return True
        else:
            print("Doesn't have battery")
            self.power_type = 0
            return False
    
    def alert_sensor(self):
        if self.energy < 20:
            return "Energy low!! charge the sensor"
        
    def charging(self):
        print('power type: ', self.power_type)
        if self.power_type == 0 and self.energy<0.505:
            self.energy += self.P_CHARGING
            print('energy: ', self.energy)
            return self.energy
        else:
            self.power_type = 1
            return self.energy
    
    
    
    
        
        
        
        