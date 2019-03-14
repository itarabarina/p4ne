#!/usr/local/bin/python3

from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, start_1=0, stop_1=100):
        IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(start_1, stop_1), False), strict = False)



    def regular(self):
        if self.is_global: return True
        else: return False

list_ip = []

for i in range(0, 50):
    network1=IPv4RandomNetwork(8, 24)
    list_ip.append(network1)

for i in list_ip:
    print(i)

