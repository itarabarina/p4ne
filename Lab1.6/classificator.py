#!/usr/local/bin/python3

import glob
import re
from ipaddress import IPv4Interface

def classificator(x):
    i = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", x)
    m = re.match("^interface (.+)", x)
    k = re.match("^hostname (.+)", x)
    if i:
        return {"ip": IPv4Interface(str(i.group(1)))}
    if m:
        return {"int": m.group(1)}
    if k:
        return {"host": k.group(1)}
    return {}

list_ipaddress=[]
list_interface=[]
list_hostname=[]

for current_file in glob.glob("/home/irina/Projects/python/Seafile/p4ne_training/config_files/*.txt"):
   with open(current_file) as f:
       for line in f:
           l=classificator(line)
           if "ip" in l: list_ipaddress.append(l)
           if "int" in l: list_interface.append(l)
           if "host" in l: list_hostname.append(l)

print(list_interface)
print(list_ipaddress)
print(list_hostname)
