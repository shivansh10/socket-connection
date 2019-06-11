#!/usr/local/bin/python2


import socket


recv_ip="127.0.0.1"
recv_port=4444 # 0  - 1024 - - you can check netstat -nulp

#creating udp socket
#ip type v4 , udp

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending data to target

s.sendto("hello",(recv_ip,recv_port))
