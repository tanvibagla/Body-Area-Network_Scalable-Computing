import time, threading

from Sensors.pacemaker import Pacemaker
from Sensors.temperature_sensor import TemperatureSensor
from Sensors.bloodoxylevel_sensor import OxySensor
from Sensors.sugarlevel_sensor import InsulinSensor
from Sensors.bloodpressure_sensor import BpSensor
from Sensors.ecglevel_sensor import EcgSensor
from Sensors.lacticacid_sensor import LacticSensor

def pm_send_data():
    print("PACEMAKER SENDING DATA")
    # threading.Timer(10, pm.send_data).start()
    pm.send_data()
    threading.Timer(pm.duty_cycle, pm_send_data).start()
    threading.Timer(1, pm.battery_decay_while_idle).start()
    threading.Timer(1, pm.battery.have_energy).start()
    if(pm.power < pm.battery.E_MIN):
        pm.battery.charging()
        threading.Timer(1, pm.battery.charging).start()
    print("battery while charging: ", pm.power)

def temp_send_data():
    print('TEMPERATURE_SENSOR SENDING DATA')
    tmp.send_data()
    threading.Timer(tmp.duty_cycle, temp_send_data).start()
    threading.Timer(1, tmp.battery_decay_while_idle).start()
    threading.Timer(1, tmp.battery.have_energy).start()

def ins_send_data():
    print('INSULIN_LEVEL_SENSOR SENDING DATA')
    ins.send_data()
    threading.Timer(ins.duty_cycle, ins_send_data).start()
    threading.Timer(1, ins.battery_decay_while_idle).start()
    threading.Timer(1, ins.battery.have_energy).start()

def oxy_send_data():
    print('OXYGEN_LEVEL_SENSOR SENDING DATA')
    oxy.send_data()
    threading.Timer(oxy.duty_cycle, oxy_send_data).start()
    threading.Timer(1, oxy.battery_decay_while_idle).start()
    threading.Timer(1, oxy.battery.have_energy).start()

def bp_send_data():
    print('BP_LEVEL_SENSOR SENDING DATA')
    bp.send_data()
    threading.Timer(bp.duty_cycle, bp_send_data).start()
    threading.Timer(1, bp.battery_decay_while_idle).start()
    threading.Timer(1, bp.battery.have_energy).start()

def ecg_send_data():
    print('ECG_LEVEL_SENSOR SENDING DATA')
    ecg.send_data()
    threading.Timer(ecg.duty_cycle, ecg_send_data).start()
    threading.Timer(1, ecg.battery_decay_while_idle).start()
    threading.Timer(1, ecg.battery.have_energy).start()

def lactic_send_data():
    print('LACTIC_LEVEL_SENSOR SENDING DATA')
    lactic.send_data()
    threading.Timer(lactic.duty_cycle, lactic_send_data).start()
    threading.Timer(1, lactic.battery_decay_while_idle).start()
    threading.Timer(1, lactic.battery.have_energy).start()


pm = Pacemaker(100, 10, {}, 'HeartRate', 1)
tmp = TemperatureSensor(100, 20, {}, 'BodyTemperature', 1)
ins= InsulinSensor(100,30,{}, 'InsulinLevel', 1)
oxy= OxySensor(100,40,{},'Oxygenlevel', 1)
bp= BpSensor(100,50,{},'BPlevel',1)
ecg= EcgSensor(100,60,{},'Ecglevel',1)
lactic= LacticSensor(100,70,{},'Lacticlevel',1)

pm_send_data()
temp_send_data()
ins_send_data()
oxy_send_data()
bp_send_data()
ecg_send_data()
lactic_send_data()

# import time, threading
# def foo():
#     print(time.ctime())
#     threading.Timer(10, foo).start()
#
# foo()