#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet, CLI
from mininet.util import irange 
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.node import RemoteController

'''
Controlador: 
cd $POX_HOME
./pox.py log.level --DEBUG openflow.of_01 --port=6653 forwarding.l2_learning 


Para correr: 
sudo python topo_test.py 
'''


class TopoTest(Topo):
   "Linear topology of k switches, with one host per switch."

   def __init__(self, nSwitch = 2, nHosts = 4, **opts):
       """Init.
           nSwitch: number of switches
           nHosts: numero de hosts
           hconf: host configuration options
           lconf: link configuration options
        """

       super(TopoTest, self).__init__(**opts)

       self.nSwitch = nSwitch
       self.nHosts = nHosts
       h = 0 #nHosts - 1
       lastSwitch = None
       for i in irange(1, nSwitch):
           switch = self.addSwitch('s%s' % i)
           for j in irange(h + 1, h + nHosts):
               # bw = 10 Mbps
               host = self.addHost('h%s' % j, mac='00:00:00:00:00:0' + str(j))
               self.addLink(switch, host, bw = 10)
           if lastSwitch:
               # bw = 10 Mbps
               self.addLink(switch, lastSwitch, bw = 2000)
           lastSwitch = switch
           h += nHosts


def simpleTest():
   info('*** Create and test a simple network ***\n')
   topo = TopoTest()

   info('*** Create the controller ***\n')
   c0 = RemoteController('c0',port = 6653)
   info(c0)
    
   net = Mininet(topo = topo, link=TCLink, build = False)
   num_ini = 1
   num_end = 1
   # Asignando una MAC determinada a las interfaces de los switches
   for s in net.switches:
       for i in s.intfs.values()[1:]:
           print i
           s.intf(str(i)).setMAC(str(num_ini) + "0:00:00:00:00:0" + str(num_end))
           num_end += 1
       num_end = 1
       num_ini += 1

   net.addController(c0)
   info('*** Build the network\n')
   net.build()
   info('*** Starting network\n')
   net.start()
   info('*** Running CLI\n')
   CLI(net)
   info('*** Stopping network')
   net.stop()


if __name__ == '__main__':
   # Tell mininet to print useful information
   setLogLevel('info')
   simpleTest()

