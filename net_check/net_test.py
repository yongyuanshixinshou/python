#!/usr/bin/python
# -*- coding: utf-8 -*-

from scapy.all import srp, Ether, ARP
IpScan = '192.168.1.0/24'
try:
    ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(hwtype=1, ptype=0x0800,op=1,pdst=IpScan), timeout=10)
except Exception as e:
    print(e)
else:
    for send, rcv in ans:
        ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")
        print(ListMACAddr)