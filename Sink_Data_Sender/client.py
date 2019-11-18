# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:19:29 2019

@author: yesh2
"""

import socket
import threading
import os

from buffer import Buffer

HOST = 'localhost'
PORT = 58575

def send_files():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    with s:
        sbuf = Buffer(s)

        hash_type = '#na'#input('Enter hash type: ')

        #files = input('Enter file(s) to send: ')
        #files_to_send = files.split()
        files_to_send = os.listdir('..\\Receiver\\')
        print('files: ', files_to_send)
        for file_name in files_to_send:
            if '.json' in file_name:
                print(file_name)
                sbuf.put_utf8(hash_type)
                sbuf.put_utf8(file_name)

                file_size = os.path.getsize('..\\Receiver\\'+file_name)
                sbuf.put_utf8(str(file_size))

                with open('..\\Receiver\\'+file_name, 'rb') as f:
                    sbuf.put_bytes(f.read())
                print('File Sent')
    threading.Timer(5, send_files).start()

send_files()