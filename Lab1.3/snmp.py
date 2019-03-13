#!/usr/local/bin/python3

from pysnmp.hlapi import *


result_get=getCmd(SnmpEngine(),
              CommunityData('public', mpModel=0),
              UdpTransportTarget(('10.31.70.107', 161)),
              ContextData(),
              ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

result_next=nextCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget(('10.31.70.107', 161)),
               ContextData(),
               ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
               lexicographicMode=False)

for i in result_get:
    errorIndication, errorStatus, errorIndex, varBinds = i
    if errorIndication: print(errorIndication)
    elif errorStatus: print(errorStatus)
    elif errorIndex: print(errorIndex)
    else:
        for x in varBinds: print(x)

for i in result_next:
    errorIndication, errorStatus, errorIndex, varBinds = i
    if errorIndication: print(errorIndication)
    elif errorIndex: print(errorIndex)
    elif errorStatus: print(errorStatus)
    else:
        for x in varBinds: print(x)
