#!/usr/local/bin/python3

import glob

list_ip = set()

for current_file in glob.glob("/home/irina/Projects/python/Seafile/p4ne_training/config_files/*.txt"):
   with open(current_file) as f:
       for line in f:
           if line.find("ip address") == 1:
               line=line.replace("ip address", "")
               list_ip.add(line.strip())

for i in list_ip:
    print(i)




