# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:43:21 2019

@author: yesh2
"""

import socket
import tqdm
import os

SEPARATOR = " "
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "localhost"
# the port, let's use 5001
port = 58575
# the name of file we want to send, make sure it exists
# filename = "..\\Receiver\\Pacemaker_Data.json"
# get the file size
# filesize = os.path.getsize(filename)

files = os.listdir('..\\Receiver\\')
print('files: ', files)

# create the client socket
s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
# s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
# s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
# progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
for file in files:
    s.connect((host, port))
    file = '..\\Receiver\\'+file
    if '.json' in file:
        filesize = os.path.getsize(file)
        s.send(f"{file}{SEPARATOR}{filesize}".encode())
        progress = tqdm.tqdm(range(filesize), f"Sending {file}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(file, "rb") as f:
            for _ in progress:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure transimission in
                # busy networks
                s.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
        # close the socket
    s.close()