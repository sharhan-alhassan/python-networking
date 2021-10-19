
import nmap

scanning_tool = nmap.PortScanner()      # Create scanning tool object

scanning_tool.scan('159.89.83.229', '21-443')  # Scan localhost for ports range [21-443]

for host in scanning_tool.all_hosts():
    print('Host: {} ({})'.format(host, scanning_tool[host].hostname()))
    print('State: {}'.format(scanning_tool[host].state()))

    for proto in scanning_tool[host].all_protocols():       # list all protocols (tcp, udp, etc)
        print('----------------------------')
        print('Protocol : {}'.format(proto))

        lport = scanning_tool[host][proto].keys()           # list all port numbers running on the protocol(eg; 22, 80,)
        #lport.sort()
        for port in lport:
            # list state(open/close) of each port running on the protocol(tcp,udp,etc)
            print("Port : {}, Name: {}, State: {}, Reason: {}".format(port, scanning_tool[host][proto][port]['name'], scanning_tool[host][proto][port]['state'], scanning_tool[host][proto][port]['reason']))

            #print ('port : %s\tstate : %s' % (port, scanning_tool[host][proto][port]['state']))
