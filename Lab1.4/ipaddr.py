#!/usr/local/bin/python3

from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, start_1=0, stop_1=100):
        IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(start_1, stop_1), False), strict = False)

    def regular(self):
        if self.is_global: return 1
        elif self.is_multicast or self.is_unspecified or self.is_private or self.is_loopback or self.is_link_local: return 0

#    def key_value(self):
#        return int(IPv4Network.network_address) + int(IPv4Network.netmask)

    def key_value(self):
        return (self.netmask, self.network_address)

list_ip = []

for i in range(0, 50):
    network1=IPv4RandomNetwork(8, 24)
    if network1.regular(): list_ip.append(network1)

def key_sort(x):
    return x.key_value()

list_sort=sorted(list_ip, key=key_sort)

for i in list_sort:
    print(i)

