# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:14:17 2019

@author: yesh2
"""

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "127.0.0.1" #10.6.34.166"  #Ip address that the TCPServer  is there
port = 50000                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
s.send("Hello")