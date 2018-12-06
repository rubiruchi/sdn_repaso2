#!/usr/bin/python
'''

Comentarios antes de compilar:
1. Toco actualizar cryptography: sudo pip install --upgrade cryptography
2. Si la imagen de Docker no esta creada es necesario crearla previamente: sudo docker build -t local_test_machine1 .
3. Se verifico que estuviera la imagen localmente: sudo docker images | grep local_test_machine1 

https://medium.com/the-code-review/top-10-docker-commands-you-cant-live-without-54fb6377f481


sudo docker kill $(sudo docker ps -q)
sudo  docker rm $(sudo docker ps -a -q)


https://opennetworkingblog.blogspot.com/2016/07/openvswitch-command-line-interface.html


https://www.tecmint.com/ifconfig-command-examples/


ifconfig eth0 172.17.1.1


Topologia:
   
Pendiente ...

sudo python topology_test1.py 


Controlador: 
sudo docker run --name c0 -p 6653:6653 -it --rm osrg/ryu /bin/bash


sudo docker run --name c0 -p 6653:6653 -it --rm sonatanfv/sonata-ryu-vnf /bin/bash


Ya una vez dentro del contenedor:

cd ryu
ryu-manager --ofp-tcp-listen-port 6653 ryu/app/simple_switch_13.py 


'''


from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.cli import CLI
from mininet.net import Containernet
from mininet.log import info, setLogLevel

import os


# Variables del programa 

num_machines = 6  # Numero de hosta
hosts = []            # Host normales
links = []
setLogLevel('info')

info('*** Create the controller \n')
c0 = RemoteController('c0', ip = "172.17.0.10", port = 6653)
info(c0)
" Create Simple topology example."
net = Containernet(build=False)
# Initialize topology
 
# Add containers
info('*** Adding docker containers using local_test_machine1 images\n')

# Agregando host de la red
for i in range(0,num_machines):
  hosts.append(net.addDocker('h' + str(i+1), ip='10.0.0.' + str(i + 1), dimage="local_test_machine1"))

# Agregando host de medida
c_h100 = net.addDocker('c_h100', ip='10.0.0.100', dimage="local_test_machine1")
s_h200 = net.addDocker('s_h200', ip='10.0.0.200', dimage="local_test_machine1")



# Add switches    
info('*** Adding switches\n')


# toco estos numero que es el de la red IP(docker0) = 172.17.0.1 --> Para mas detalle ver: https://www.quora.com/How-do-I-assign-a-static-IP-to-a-docker-container 

s1 = net.addSwitch('s1', ip='172.17.0.20', protocols='OpenFlow13') #...
s2 = net.addSwitch('s2', ip='172.17.0.30', protocols='OpenFlow13') #...

# Add links    
info('*** Creating links\n')
for i in range (num_machines//2):
  #links.append(net.addLink(hosts[i], s1, bw=10))  # Actualizar velocidades
  links.append(net.addLink(hosts[i], s1))

for i in range (num_machines//2 + 1, num_machines):
  #links.append(net.addLink(hosts[i], s2, bw=10))  # Actualizar velocidades
  links.append(net.addLink(hosts[i], s2)) 

links.append(net.addLink(c_h100, s1))
links.append(net.addLink(s_h200, s2))

#links.append(net.addLink(s1, s2, bw = 2000))
links.append(net.addLink(s1, s2))

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


'''
containernet> nodes
available nodes are: 
c0 client_h100 h1 h2 h3 h4 h5 h6 s1 s2 server_h200
containernet> net
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
h3 h3-eth0:s1-eth3
h4
h5 h5-eth0:s2-eth1
h6 h6-eth0:s2-eth2
client_h100
server_h200
s1 lo:  s1-eth1:h1-eth0 s1-eth2:h2-eth0 s1-eth3:h3-eth0 s1-eth4:s2-eth3
s2 lo:  s2-eth1:h5-eth0 s2-eth2:h6-eth0 s2-eth3:s1-eth4
c0
containernet> links
h1-eth0<->s1-eth1 (OK OK)
h2-eth0<->s1-eth2 (OK OK)
h3-eth0<->s1-eth3 (OK OK)
h5-eth0<->s2-eth1 (OK OK)
h6-eth0<->s2-eth2 (OK OK)
s1-eth4<->s2-eth3 (OK OK)

 sudo ovs-vsctl show
9ec06414-9bd9-4579-81d4-8e7801c2eb61
    Bridge "s2"
        Controller "tcp:172.17.1.1:6653"
        fail_mode: secure
        Port "s2-eth2"
            Interface "s2-eth2"
        Port "s2-eth1"
            Interface "s2-eth1"
        Port "s2-eth3"
            Interface "s2-eth3"
        Port "s2"
            Interface "s2"
                type: internal
    Bridge "s1"
        Controller "tcp:172.17.1.1:6653"
        fail_mode: secure
        Port "s1-eth3"
            Interface "s1-eth3"
        Port "s1"
            Interface "s1"
                type: internal
        Port "s1-eth2"
            Interface "s1-eth2"
        Port "s1-eth1"
            Interface "s1-eth1"
        Port "s1-eth4"
            Interface "s1-eth4"
    ovs_version: "2.5.5"


'''
