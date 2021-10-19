
## Resource:
[Resource Link](https://www.studytonight.com/network-programming-in-python/introduction-to-network-programming)

## IP address is of two types:

- Private IP address: Ranges from (192.168.0.0 – 192.168.255.255), (172.16.0.0 – 172.31.255.255) or (10.0.0.0 - 10.255.255.255)

- Public IP address: A public IP address is an IP address that your home or business router receives from your ISP(Internet Service Provider).

- Sockets are the endpoints of a bidirectional, point-to-point communication channel. Given an internet connection, say between `client(a browser)` and the `server(say cloudbintech.com)`, we will have two sockets. A Client Socket and a Server Socket.

- Socket acts on two parts: `IP Address + Port Number`

- source machine(eg:browser)      ------->  Destination machine(cloudbintech.com)
  192.168.1.1:1300                ------->  cloudbintech.com:80
  IP Address + Port (`Ephermal`)  ------->  IP Address + Port (standard/well defined port)

- When the client tries to connect with the server, a random port is assigned by the operating system for the connection. This random port is called `Ephermal Port`. In the above illustration, `1300` is an ephermal port on the source(client) machine.

- NB: `The client socket is short lived, i.e as soon as the data exchange ends it closes.`

## Sample Socket connection when you visit www.cloudbintech.com

```python
#A socket object is created for communication
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now connect to the web server on port 80 (normal http port)
clientsocket.connect(("cloudbintech.com", 80))

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to a public host and a well-known port
serversocket.bind((socket.hostname(), 80))

#become a server socket and listen for connections
serversocket.listen(5)
```

### Connect in client VS Bind in Server
- connect method is used `client(eg;browser)` to establish temporary connection with port 80 on the server IP. 

- bind method creates/assign a permanent port number (80) to the server IP and match the hostname to the port number. Thus binding the hostname to the port. Eg; `cloudbintech.com:80`. This is bind permanently because the hostname/IP needs to be up and running all the time to receive traffic from everywhere. Eg; youtube.com's port 80(http) or https(443) needs to binded and up and running 24/7

## Types of Python Sockets
- There are basically two types of sockets: `SOCK_STREAM` and `SOCK_DGRAM`

SOCK_STREAM                             SOCK_DGRAM
1. For TCP Protocols                    2. For UDP Protocols

### Socket Module
- We use `socket.socket()` function which has the syntax:
`S = socket.socket(socket_family, socket_type, protocol=0)`

- `socket_family`: This is either `AF_UNIX` or `AF_INET`
- `socket_type` : This is either `SOCK_STREAM` or `SOCK_DGRAM`
- `protocol` : Usually left out defaulting to 0


### Socket Methods
- Client socket methods
1. `connect()` : This method is for client to connect to a server(remote socket at an addres). Its syntax is `connect(host, port)` for `AF_INEX` address family

- Server socket methods
1. `bind()` : This method binds the socket to an address. The format of address depends on socket family mentioned above(AF_INET).

2. `listen(backlog)` : This method listens for the connection made to the socket. The backlog is the maximum number of queued connections that must be listened before rejecting the connection.

3. `accept()` : This method is used to accept a connection. The socket must be bound to an address and listening for connections. The return value is a `pair(conn, address)` where `conn is a new socket object which can be used to send and receive data on that connection`, and `address is the address bound to the socket on the other end of the connection`


### Some other General Socket Methods
- `TCP Socket Methods`              	    - `UDP Socket Methods`
1. s.recv()→ Receives TCP messages	        s.recvfrom()→ Receives UDP messages
2. s.send()→ Transmits TCP messages	        s.sendto()→ Transmits UDP messages


### Some Basic Socket Methods
1. `close()` : This method is used to close the socket connection.

2. `gethostname()` : This method returns a string containing the hostname of the machine where the python interpreter is currently executing. For example: localhost.

3. `gethostbyname()` :  If you want to know the current machine's IP address, you may use `gethostbyname(gethostname())`.


### Blocking and Non-Blocking Socket I/O
- By Default, `setblocking(1)` is set to `1`. This means that, client will wait for operations to complete such that when you call `send()` it'll put the data in the buffer and send it in chunks till it finishes.

- Unlike `setblocking(0)`, it never waits for the operation to complete. when the `send()` method is called it'll put as much data it can on the buffer and return

### Encrypting sockets with TSL/SSL
- Data(plaintext) --> Encryption(algorithm) -->Data(ciphertext) -->Decryption -->Data(plaintext)


## Port Scanner
- Ports are like `doors/windows` or any entrance to a building

- The Building is the `IP Address`

- You therefore would want to regularly scan opening ports for your `system(server)` to enforce security purposes


### Nmap Port Scamming
- `nmap (Network Mapper)` : A security scanner for discovering hosts and services on a computer network, thereby building a map of the network. 

- nmap sends specially crafted packets to the target host(s) and then analyzes their responses

### Some nmap features include:

1. `Host Discovery`: Identify any hosts on any network. Eg: List hosts that respond to TCP and/or ICMP requests or have a particular `port` open

2. `Port Scanning` : Counting and listing one by one all open ports on the target

3. `Version Detection` : Interrogate network services on remote devices to determine application name and version number

4. `OS Detection` : Determin OS system and hardware characteristics of the network devices

5. `Scriptable interaction with the target` : Using Nmap Scripting Engine `(NSE)` and Lua programming language, we can easily write scripts to perform operations on the network devices

- `zenmap` is the GUI for `nmap`


### Nmap Port Scanning Script with Input from CLI
- We'll take input from CLI using two ways

1. `argparse` :

2. `optparse` :


### Banner Grabbing:
- A `Banner` is like a text message received from the host. It contains information about the services running on the host along with information about the ports.

- `Banner Grabbing` is a technique generally used by the System administrators to scan the network to check what `all services` are running etc.

- Some of the known ports and services are:
```bash
20/21: FTP
22: SSH(Secure Shell)
23: Telnet
25: SMTP
80: HTTP
156: SQL Server
443: HTTPS
```

- Just knowing about the available ports and services running is not enough. You must know about the specifics of the service running like `version of the server` that the host is running, eg; `version of MySQL` etc.


### Banner Grabbing using Nmap
We have already learnt how to use Nmap for port scanning, here is a simple command which can be used for Banner Grabbing using Nmap.

The command below will scan all the open ports on the host.

```bash
nmap -sV –script=banner 127.0.0.1
```

In case you want to grab banner(information) related to a particular port only, then run the following command:

```bash
nmap -Pn -p 80 -sV –script=banner 127.0.0.1
```

### Using Wireshark for Network Traffic Analysis

- `Network Traffic` or `Network Data` is the amount of `data(packets)` moving across a network at any given point of time.

- `Traffic volume = Traffic Intensity * Time`

- `Wireshark` : Is a packet analyser

- `tcpdump` : Is used to capture traffic. 

- Wireshark allows you to save file in multiple extensions but for our purpose we will use `.pcap` extension

- Installing `Wireshark`:
```bash
$ sudo apt-get install wireshark
```

### Using dpkt to analyze traffic
- `dpkt` is a python library for packet creation/parsing with definition for the basic TCP/IP protocols

- Installation process

```bash
$ sudo pip install dpkt
```
- Using the `dpkt` library, we will extract the `source IP` and `destination IP` addressess for the packets on the network using python code, from our `.pcap file`, in which we saved the Workshire traffic data.


### Scapy: Another Python module
- This is a python module that allows us to:
```python
1. send
2. sniff 
3. dissect and 
4. forge network packets
```

- It's a CLI utility tool

This capability allows construction of tools that can `probe, scan or attack networks`.

### Installing scapy
```bash
$ sudo pip install scapy
```

### To Run it
```bash
$ sudo scapy
```

### Reading files
- `Scapy` can read pcap files and write them to another pcap file

- Sample output
```bash
>>> rdpcap('wlo1-capture.pcap')
<wlo1-capture.pcap: TCP:1491 UDP:1782 ICMP:0 Other:2>
>>> 

```