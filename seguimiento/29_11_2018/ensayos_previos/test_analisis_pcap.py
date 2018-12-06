import sys

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.link import TCLink

from time import time
from select import poll, POLLIN
from subprocess import Popen, PIPE
from time import sleep


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
               host = self.addHost('h%s' % j)
               self.addLink(switch, host, bw = 10)
           if lastSwitch:
               # bw = 1 Gbps
               self.addLink(switch, lastSwitch, bw = 10)
           lastSwitch = switch
           h += nHosts

def test_ping():
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    net.pingAll()
    net.stop()

def test_iperf():
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    net.iperf()
    net.pingAll()
    net.stop()

# No se hace nada, no se mide nada
def test_empty():
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    sleep(60)
    net.stop()

# No se hace nada, no se mide nada
def test_iperf2():
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    sleep(30)
    net.iperf()
    net.stop()

def test_spoof_attack():
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    net_links = net.links
    for l in net_links:
        print l
    sleep(20)  # Tiempo para configurar wireshark
    net.get('h1').cmdPrint('hping3 --rand-source', str(net.get('h8').IP()), "&")
    sleep(60)
    net.stop()

def test_flood_attack():
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    net_links = net.links
    for l in net_links:
        print l
    sleep(20)  # Tiempo para configurar wireshark
    net.get('h1').cmdPrint('hping3 --flood', str(net.get('h8').IP()), "&")
    sleep(60)
    net.stop()

def test_flood_spoof_attack():
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    net_links = net.links
    for l in net_links:
        print l
    sleep(20)  # Tiempo para configurar wireshark
    net.get('h1').cmdPrint('hping3 --flood --rand-source', str(net.get('h8').IP()), "&")
    sleep(60)
    net.stop()


if __name__ == '__main__':
    print ("*** Empezando el ensayo ***")
    setLogLevel('info')
    # test_empty()
    # test_iperf()
    # test_iperf2()
    # test_spoof_attack()
    # test_flood_attack()
    test_flood_spoof_attack()
    print ("*** Hasta la vista baby ***")


