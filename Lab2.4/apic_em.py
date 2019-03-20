#!/usr/local/bin/python3

import requests, json, pprint
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("topology.html")

@app.route('/api/topology')
def topology():
    return jsonify(responce_topology.json()['response'])

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser",
               "password": "Cisco123!"
              }
    header = {"content-type": "application/json"}

    response = requests.post(url, data=json.dumps(payload),
                             headers=header, verify=False)

    return response.json()['response']['serviceTicket']

if __name__ == '__main__':

    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url_host = "https://" + controller + "/api/v1/host?limit=1&offset=1"
    url_network_device = "https://" + controller + "/api/v1/network-device"
    url_topology = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json",
              "X-Auth-Token":ticket
             }

    responce_host = requests.get(url_host, headers=header, verify=False)
    responce_network_device = requests.get(url_network_device, headers=header, verify=False)
    responce_topology = requests.get(url_topology, headers=header, verify=False)

#    print("Hosts = ")
    pprint.pprint(json.dumps(responce_host.json()))
    pprint.pprint(responce_network_device.json())
    pprint.pprint(responce_topology.json())

app.run(debug=True)
