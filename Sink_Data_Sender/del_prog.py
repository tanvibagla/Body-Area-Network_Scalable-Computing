# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:10:19 2019

@author: rajaredy
"""

import os 

def del_files(path,filename):
    print("File received to delete  "+filename)
    path = path
    if len(os.listdir(path)):
        for file in os.listdir(path):
            if '.json' in file and filename == file:
                os.remove(os.path.join(path,file))
                print("Deleted: "+file)
    else:
        print("Files transfered deleting files!")
        print("No files exists!")

    
