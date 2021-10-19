
import nmap
import optparse

def nmapScan(tgtHost, tgtPort):
    nmscan = nmap.PortScanner()
    nmscan.scan(tgtHost, tgtPort)
    state = nmscan[tgtHost]['tcp'][int(tgtPort)]['state']
    # print('Scanning for ports...')
    print('[*] ' + tgtHost + ' tcp/' + tgtPort + ' ' + state)


def main():
    parser = optparse.OptionParser('Script Usage:' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')

    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port(s) separated by comma')

    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort)

    # print(tgtPorts)

    if (tgtHost == None) | (tgtPorts[0] == None):
        print (parser.usage)
        exit(0)
    
    ports = tgtPorts.strip("'").split(',')

    for tgtPort in ports:
        # print (tgtHost+ " " + tgtPort)
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()
    
