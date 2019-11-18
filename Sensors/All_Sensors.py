import time, threading

from Sensors.pacemaker import Pacemaker
from Sensors.temperature_sensor import TemperatureSensor
from Sensors.bloodoxylevel_sensor import OxySensor
from Sensors.sugarlevel_sensor import InsulinSensor

def pm_send_data():
    print("PACEMAKER SENDING DATA")
    # threading.Timer(10, pm.send_data).start()
    pm.send_data()
    threading.Timer(pm.duty_cycle, pm_send_data).start()

def temp_send_data():
    print('TEMPERATURE_SENSOR SENDING DATA')
    tmp.send_data()
    threading.Timer(tmp.duty_cycle, temp_send_data).start()

def ins_send_data():
    print('INSULIN_LEVEL_SENSOR SENDING DATA')
    ins.send_data()
    threading.Timer(ins.duty_cycle, ins_send_data).start()

def oxy_send_data():
    print('OXYGEN_LEVEL_SENSOR SENDING DATA')
    oxy.send_data()
    threading.Timer(ins.duty_cycle, oxy_send_data).start()


pm = Pacemaker(100, 10, {}, 'HeartRate', 1)
tmp = TemperatureSensor(100, 20, {}, 'BodyTemperature', 1)
ins= InsulinSensor(100,30,{}, 'InsulinLevel', 1)
oxy= OxySensor(100,40,{},'Oxygenlevel', 1)

pm_send_data()
temp_send_data()
ins_send_data()
oxy_send_data()

# import time, threading
# def foo():
#     print(time.ctime())
#     threading.Timer(10, foo).start()
#
# foo()