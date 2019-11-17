import time, threading

from Sensors.pacemaker import Pacemaker
from Sensors.temperature_sensor import TemperatureSensor

def pm_send_data():
    print("PACEMAKER SENDING DATA")
    # threading.Timer(10, pm.send_data).start()
    pm.send_data()
    threading.Timer(pm.duty_cycle, pm_send_data).start()

def temp_send_data():
    print('TEMPERATURE_SENSOR SENDING DATA')
    tmp.send_data()
    threading.Timer(tmp.duty_cycle, temp_send_data).start()

pm = Pacemaker(100, 30, {}, 'HeartRate', 1)
tmp = TemperatureSensor(100, 120, {}, 'BodyTemperature', 1)

pm_send_data()
temp_send_data()

# import time, threading
# def foo():
#     print(time.ctime())
#     threading.Timer(10, foo).start()
#
# foo()