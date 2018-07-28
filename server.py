#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 22:56:53 2018

@author: ryblog
"""

import socket
import pickle

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buffer = connection.recv(4096)#64)
    if len(buffer) > 0:
        buffer = pickle.loads(buffer)
        if buffer == 'close':
            break
        print(buffer)
        print(buffer[0])
        
serversocket.close()