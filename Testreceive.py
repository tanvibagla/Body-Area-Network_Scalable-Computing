# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:26:53 2019

@author: yesh2
"""


import socket                   # Import socket module
#netstat -ano| find portnum #output port status with PID
#taskkill /F /PID <process ID>
port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = ""   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')


while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from ', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='File2send\\sensor.json' #In the same folder or path is this file running must the file you want to tranfser to be
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()




'''
# first of all import the socket library 
import socket                
  
# next create a socket object 
s = socket.socket()          
print("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 21128                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening")          


while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print('Got connection from', addr) 
   
   with open('File2send\\received_file', 'wb') as f:
       print('file opened')
       while True:
           print('receiving data...')
           data = s.recv(1024)
           print('data=%s', (data))
           if not data:
            break
        # write data to a file
            f.write(data)
    #f.close()
  
   # send a thank you message to the client.  
   c.send('Thank you for connecting') 
  
   # Close the connection with the client 
   c.close() 

print('Successfully get the file')
s.close()
'''