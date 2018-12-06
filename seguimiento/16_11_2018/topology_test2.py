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

https://github.com/mininet/mininet/blob/master/examples/scratchnetuser.py
https://github.com/mininet/mininet/blob/master/examples/linearbandwidth.py
https://github.com/mininet/mininet/pull/650/files
https://www.programcreek.com/python/example/106419/mininet.link.TCLink

'''


'''
Comandos ejecutados: 

Topologia: 

sudo python topology_test2.py 

Controlador

sudo docker run -h c0 --name c0 -p 6653:6653 -it --rm sonatanfv/sonata-ryu-vnf /bin/bash
cd ryu
ryu-manager --ofp-tcp-listen-port 6653 ryu/app/simple_switch_13.py 


Interaccion: basandonos en: http://csie.nqu.edu.tw/smallko/sdn/iperf_mininet.htm


containernet> nodes
available nodes are: 
c0 client_h100 h1 h2 h3 h4 h5 h6 s1 s2 server_h200

containernet> links
h1-eth0<->s1-eth1 (OK OK)
h2-eth0<->s1-eth2 (OK OK)
h3-eth0<->s1-eth3 (OK OK)
h5-eth0<->s2-eth1 (OK OK)
h6-eth0<->s2-eth2 (OK OK)
s1-eth4<->s2-eth3 (OK OK)
c_h100-eth0<->s1-eth5 (OK OK)
s_h200-eth0<->s2-eth4 (OK OK)

containernet> net
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
h3 h3-eth0:s1-eth3
h4
h5 h5-eth0:s2-eth1
h6 h6-eth0:s2-eth2
c_h100 c_h100-eth0:s1-eth5
s_h200 s_h200-eth0:s2-eth4
s1 lo:  s1-eth1:h1-eth0 s1-eth2:h2-eth0 s1-eth3:h3-eth0 s1-eth4:s2-eth3 s1-eth5:c_h100-eth0
s2 lo:  s2-eth1:h5-eth0 s2-eth2:h6-eth0 s2-eth3:s1-eth4 s2-eth4:s_h200-eth0
c0



containernet> xterm client_h100 server_h200

root@client_h100:/# 

( O tambien ---

sudo docker ps
sudo docker exec -it mn.server_h200 bash
sudo docker exec -it mn.client_h100 bash

)

mn.server_h200
iperf -s -p 2000 -i 1 2>&1 | tee server_bw.log

///// Desordenado...

sudo docker ps
sudo docker exec -it mn.s_h200 bash
cd /mnt/bw_logs/
iperf3 -s -i 1 > server_bw1.log

iperf3 -s -i 1 > server_bw2.log

iperf3 -s -i 1 > server_bw3.log

sudo docker exec -it mn.c_h100 bash
iperf3 -c 10.0.0.200 -t 150

https://support.cumulusnetworks.com/hc/en-us/articles/216509388-Throughput-Testing-and-Troubleshooting#iperf3

sudo docker exec -it mn.h1 bash
hping3 --flood --rand-source 10.0.0.5

sudo docker exec -it mn.h2 bash
hping3 --flood --rand-source 10.0.0.5

sudo docker exec -it mn.h3 bash
hping3 --flood --rand-source 10.0.0.5


https://support.cumulusnetworks.com/hc/en-us/articles/216509388-Throughput-Testing-and-Troubleshooting#iperf3



packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 2 5a:2c:f8:70:3c:23 33:33:00:00:00:02 3

///////////////////////////////////////////////////

containernet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 X h5 h6 c_h100 s_h200 
h2 -> h1 h3 X h5 h6 c_h100 s_h200 
h3 -> h1 h2 X h5 h6 c_h100 s_h200 
h4 -> X X X X X X X 
h5 -> h1 h2 h3 X h6 c_h100 s_h200 
h6 -> h1 h2 h3 X h5 c_h100 s_h200 
c_h100 -> h1 h2 h3 X h5 h6 s_h200 
s_h200 -> h1 h2 h3 X h5 h6 c_h100 
*** Results: 14% dropped (42/49 received)

packet in 1 a2:60:79:38:ee:17 ff:ff:ff:ff:ff:ff 2
packet in 2 a2:60:79:38:ee:17 ff:ff:ff:ff:ff:ff 3
packet in 2 76:89:67:2d:6d:e0 a2:60:79:38:ee:17 4
packet in 1 76:89:67:2d:6d:e0 a2:60:79:38:ee:17 4
packet in 1 a2:60:79:38:ee:17 76:89:67:2d:6d:e0 2
packet in 2 a2:60:79:38:ee:17 76:89:67:2d:6d:e0 3
packet in 1 f6:6d:95:7d:fa:08 ff:ff:ff:ff:ff:ff 3
packet in 2 f6:6d:95:7d:fa:08 ff:ff:ff:ff:ff:ff 3
packet in 2 b2:5e:17:5e:f2:2b f6:6d:95:7d:fa:08 2
packet in 1 b2:5e:17:5e:f2:2b f6:6d:95:7d:fa:08 4
packet in 1 f6:6d:95:7d:fa:08 b2:5e:17:5e:f2:2b 3
packet in 2 f6:6d:95:7d:fa:08 b2:5e:17:5e:f2:2b 3
packet in 1 f6:6d:95:7d:fa:08 ff:ff:ff:ff:ff:ff 3
packet in 2 f6:6d:95:7d:fa:08 ff:ff:ff:ff:ff:ff 3
packet in 1 6a:0f:ba:64:61:4e f6:6d:95:7d:fa:08 5
packet in 1 f6:6d:95:7d:fa:08 6a:0f:ba:64:61:4e 3
packet in 1 f6:6d:95:7d:fa:08 ff:ff:ff:ff:ff:ff 3
packet in 2 f6:6d:95:7d:fa:08 ff:ff:ff:ff:ff:ff 3
packet in 2 76:89:67:2d:6d:e0 f6:6d:95:7d:fa:08 4
packet in 1 76:89:67:2d:6d:e0 f6:6d:95:7d:fa:08 4
packet in 1 f6:6d:95:7d:fa:08 76:89:67:2d:6d:e0 3
packet in 2 f6:6d:95:7d:fa:08 76:89:67:2d:6d:e0 3
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 2 b2:5e:17:5e:f2:2b d6:fa:16:06:48:cb 2
packet in 2 d6:fa:16:06:48:cb b2:5e:17:5e:f2:2b 1
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 1 6a:0f:ba:64:61:4e d6:fa:16:06:48:cb 5
packet in 2 6a:0f:ba:64:61:4e d6:fa:16:06:48:cb 3
packet in 2 d6:fa:16:06:48:cb 6a:0f:ba:64:61:4e 1
packet in 1 d6:fa:16:06:48:cb 6a:0f:ba:64:61:4e 4
packet in 2 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 1
packet in 2 76:89:67:2d:6d:e0 d6:fa:16:06:48:cb 4
packet in 1 d6:fa:16:06:48:cb ff:ff:ff:ff:ff:ff 4
packet in 2 d6:fa:16:06:48:cb 76:89:67:2d:6d:e0 1
packet in 2 b2:5e:17:5e:f2:2b ff:ff:ff:ff:ff:ff 2
packet in 1 b2:5e:17:5e:f2:2b ff:ff:ff:ff:ff:ff 4
packet in 1 6a:0f:ba:64:61:4e b2:5e:17:5e:f2:2b 5
packet in 2 6a:0f:ba:64:61:4e b2:5e:17:5e:f2:2b 3
packet in 2 b2:5e:17:5e:f2:2b 6a:0f:ba:64:61:4e 2
packet in 1 b2:5e:17:5e:f2:2b 6a:0f:ba:64:61:4e 4
packet in 2 b2:5e:17:5e:f2:2b ff:ff:ff:ff:ff:ff 2
packet in 1 b2:5e:17:5e:f2:2b ff:ff:ff:ff:ff:ff 4
packet in 2 76:89:67:2d:6d:e0 b2:5e:17:5e:f2:2b 4
packet in 2 b2:5e:17:5e:f2:2b 76:89:67:2d:6d:e0 2



'''

from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.cli import CLI
from mininet.net import Containernet
from mininet.log import info, setLogLevel
from mininet.link import TCLink
from mininet.link import TCIntf
from mininet.link import TCLink

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

s1 = net.addSwitch('s1', ip = '172.17.0.20', protocols='OpenFlow13') #...
s2 = net.addSwitch('s2', ip = '172.17.0.30', protocols='OpenFlow13') #...

# Add links
info('*** Creating links\n')
for i in range (num_machines//2):
  links.append(net.addLink(hosts[i], s1, bw = 10))

for i in range (num_machines//2 + 1, num_machines):
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


'''
