#!/usr/bin/python
# -*- coding: latin-1 -*-


from mininet.topo import Topo
from mininet.net import Containernet, CLI
from mininet.util import irange, dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.node import OVSSwitch, Controller, RemoteController

'''
Comandos utiles:
https://www.southampton.ac.uk/~drn1e09/ofertie/openvswitch_useful_commands.txt
http://therandomsecurityguy.com/openvswitch-cheat-sheet/
https://gist.github.com/djoreilly/c5ea44663c133b246dd9d42b921f7646


Controlador: 
ryu-manager --ofp-tcp-listen-port 6653 simple_switch_13.py 


Para correr: 
sudo python topo_test.py 
'''

import os


# Variables del programa

num_machines = 6      # Numero de hosts elementales
hosts = []            # Host elementales (h1, h2, h3, h4, h5, h6)
links = []
setLogLevel('info')

info('*** Inicio de la configuración de la red ***\n')


info('*** Create the controller \n')
c0 = RemoteController('c0', port = 6653)
info(c0)

info('*** Create Simple topology example\n')

net = Containernet(build=False, link=TCLink)
# Initialize topology

# Add containers
info('*** Adding docker containers using local_test_machine1 images\n')

# Agregando host de la red
for i in range(0,num_machines):
    hosts.append(net.addDocker('h' + str(i+1), ip='10.0.0.' + str(i + 1), dimage="local_test_machine1"))

# Agregando host de medida
c_h100 = net.addDocker('c_h100', ip='10.0.0.100', dimage="local_test_machine1")
s_h200 = net.addDocker('s_h200', ip='10.0.0.200', dimage="local_test_machine1", volumes=[ os.getcwd() + "/bw_logs:/mnt/bw_logs:rw"])

# Add switches
info('*** Adding switches\n')


# toco estos numero que es el de la red IP(docker0) = 172.17.0.1 --> Para mas detalle ver: https://www.quora.com/How-do-I-assign-a-static-IP-to-a-docker-container

s1 = net.addSwitch('s1', protocols='OpenFlow13') #...
s2 = net.addSwitch('s2', protocols='OpenFlow13') #...

# Add links
info('*** Creating links\n')
for i in range (num_machines//2):
    links.append(net.addLink(hosts[i], s1, bw = 10))

for i in range (num_machines//2, num_machines):
    links.append(net.addLink(hosts[i], s2, bw = 10))

links.append(net.addLink(s1, s2, bw = 1000))

links.append(net.addLink(c_h100, s1))
links.append(net.addLink(s_h200, s2))

net.addController(c0)

# Build the network
info('*** Build the network\n')
net.build()
info('*** Starting network\n')
net.start()
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()
