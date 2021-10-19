
#!usr/bin/env python
# this code prints Source and Destination IP from the given 'pcap' file

import dpkt
import socket

def printPcap(pcap):
    for (ts, buf) in pcap:
        # ts=timestamp, buf=buffer
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)  # read the source IP in src
            dst = socket.inet_ntoa(ip.dst)  # read the dest. IP in dst
            print('Source: ' + src + 'Destination: ' + dst)
        except:
            pass

def main():
    # Open pcap file for reading
    f = open('wlo1-capture.pcap')

    # Pass the file argument to the pcap.Reader function
    pcap = dpkt.pcap.Reader(f)
    
    # Call the printPcap with the pcap as an argument 
    printPcap(pcap)


if __name__ == '__main__':
    main()
    

'''
socket methods inet_ntoa and inet_aton. inet_aton converts a 32-bit packed 
IPv4 address(a string of four characters in length) to its standard dotted-quad string 
representation(for example, 123.45.67.89).
'''