#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 00:17:27 2018

@author: ryblog
"""

import socket
import pickle

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

#clientsocket.send(bytes('close', 'UTF-8'))

data = [0, 
        12, 
        '/Users/ryblog/projects/server_client_demo/', 
        '/home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/', 
        3, 
        None,
        -1,
        'hi', 
        10, 
        3.1415926535897,
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/1/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/2/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/3/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/4/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/5/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/6/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/7/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/8/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/9/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/10/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/11/',
        'home/to/users/data/Folder/tmp/oudoor/20.5__test_12_35_21_11/12/'] 
#data = 'close'
outgoing = pickle.dumps(data)
clientsocket.send(outgoing)