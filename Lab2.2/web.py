#!/usr/local/bin/python3

from flask import Flask
import glob
import re
import pprint

hosts={}

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    help="Для получения списка имен хостов выполните запрос к /configs. Для получения списка ip адресов хоста выполните запрос на /config/<hostname> где hostname - имя выбранного хоста"
    return help

@app.route('/configs')
def list_hostname():
   name=[]
   for i in hosts.keys():
       name.append(hosts[i]['hostname'])
   return str(name)


@app.route('/config/<hostname>')
def list_ip(hostname):
    for j in hosts.keys():
        if hosts[j]['hostname'] == hostname:
            return str(hosts[j]['ip'])
        else: return "ERROR"
            
if __name__ == '__main__':

    for current_file in glob.glob("/home/irina/Projects/python/Seafile/p4ne_training/config_files/*.txt"):
        m=re.match("^.*/config_files/(.*)_([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*", current_file)
        if m: s=m.group(1)
        #print(current_file_name)
        hosts[s] = {}
        hosts[s]['ip'] = []

        with open(current_file) as f:
            for line in f:
                m = re.match("^hostname (.+)", line)
                if m:
                    hosts[s]['hostname'] = m.group(1)
                    continue
                i = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", line)
                if i:
                    hosts[s]['ip'].append(i.group(1))

pprint.pprint(hosts)

app.run(debug=True)
  
