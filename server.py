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
    buf = connection.recv(64)
    if len(buf) > 0:
        buf = pickle.loads(buf)
        print(buf)
        print(buf[0])
        if buf == 'close':
            break

serversocket.close()