# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:14:40 2019

@author: yesh2
"""

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "127.0.0.1" #10.6.34.166"  #Ip address that the TCPServer  is there
port = 50000                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
s.send("Hello")

with open('File2send\\Outfile_name', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()


print('Successfully get the file')
s.close()
print('connection closed')




'''
import socket # for socket 
import sys  
import os

# default port for socket 
port = 21128
  
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket successfully created")
except socket.error as err: 
    print("socket creation failed with error %s" %(err)) 
    
    
try: 
    #host_ip = socket.gethostbyname('www.google.com')
    host_ip = '10.6.34.166'
except socket.gaierror: 
  
    # this means could not resolve the host 
    print("there was an error resolving the host")
    sys.exit() 

# connecting to the server 
s.connect((host_ip, port)) 
  
print("the socket has successfully connected to local system == %s" %(host_ip))

#Intitialize
#df = 'path/to/data/file'
blocksize = 8192 
df = 'File2send\\sensor.json'
#Share file to different system
if os.path.exists(df):
  with open(df, 'rb') as f:
    packet = f.read(blocksize)

    while packet != '':
      s.send(packet)

      packet = f.read(blocksize)
      
      
# or some other size packet you want to transmit.  
                 # Powers of 2 are good.
#conn = socket.socket(socket.AF_INET, .SOCK_STREAM)
                 
'''