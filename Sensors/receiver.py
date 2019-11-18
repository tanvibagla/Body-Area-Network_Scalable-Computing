# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:14:04 2019

@author: yesh2
"""
import json
import socket                   # Import socket module
#netstat -ano| find portnum #output port status with PID
#taskkill /F /PID <process ID>
import threading
from Const.config import PACEMAKER_PORT, TEMP_PORT, INSULIN_PORT,OXYLEVEL_PORT,BP_PORT,ECGLEVEL_PORT,LACTIC_PORT

def make_connection(port):
    s = socket.socket()  # Create a socket object
    host = socket.gethostbyname(socket.gethostname())  # "127.0.0.1"   # Get local machine name
    s.bind((host, port))  # Bind to the port
    s.listen(5)

# port = 63342                    # Reserve a port for your service every new transfer wants a new port or you must wait.
# s = socket.socket()             # Create a socket object
# host = socket.gethostbyname(socket.gethostname()) #"127.0.0.1"   # Get local machine name
# s.bind((host, port))            # Bind to the port
# s.listen(5)                     # Now wait for client connection.

# print('Server listening....')

filename = None

def receive_data(port):
    while True:
        print("port number: ", port)
        s = socket.socket()  # Create a socket object
        host = socket.gethostbyname(socket.gethostname())  # "127.0.0.1"   # Get local machine name
        s.bind((host, port))  # Bind to the port
        s.listen(50)
        print('Server listening....')
        conn, addr = s.accept()  # Establish connection with client.
        print('Got connection from ', addr)
        data = conn.recv(1024)
        data = data.decode()
        data = json.loads(data)
        if data['sid'] == 'HeartRate':
            filename = 'Pacemaker_Data.json'
        elif data['sid'] == 'BodyTemperature':
            filename = 'BodyTemperature_data.json'
        elif data['sid'] == 'InsulinLevel':
            filename = 'InsulinLevel_data.json'
        elif data['sid'] == 'Oxygenlevel':
            filename = 'OxygenLevel_data.json'
        elif data['sid'] == 'BPlevel':
            filename = 'BpLevel_data.json'
        elif data['sid'] == 'Ecglevel':
            filename = 'EcgLevel_data.json'
        elif data['sid'] == 'Lacticlevel':
            filename = 'EcgLevel_data.json'        
        print('data type: ', type(data))
        with open(filename, '+a') as f:
            print('file opened')
            print('receiving data...')

            print('data["sid"]: ', data['sid'])
            print('data=', data)
            s.close()
            if not data:
                break
            # write data to a file
            f.write('\n' + json.dumps(data))
        f.close()

        conn.close()
        # threading.Timer(1, receive_data, [port]).start()

    print('Successfully get the file')
    # s.close()
    # conn.close()
    print('connection closed')



    # def listen_port():
#
# def receive():
receive_data(PACEMAKER_PORT)
receive_data(TEMP_PORT)
receive_data(INSULIN_PORT)
receive_data(OXYLEVEL_PORT)
receive_data(BP_PORT)
receive_data(ECGLEVEL_PORT)
receive_data(LACTIC_PORT)
# receive_data(TEMP_PORT)
