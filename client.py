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
#clientsocket.send('hello')
#clientsocket.send(bytes('close', 'UTF-8'))

y=[0,12,6,8,3,'hi',10] 
#y='close'
data=pickle.dumps(y)
clientsocket.send(data)