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
               # bw = 10 Mbps
               self.addLink(switch, lastSwitch, bw = 1000)
           lastSwitch = switch
           h += nHosts

def test_ping():
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    net.pingAll()
    net.stop()

def testBW(test_time, experimento):
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    hosts_iperf = [net.get(experimento['iperf_src']), net.get(experimento['iperf_dst'])]
    outfile = "iperf_" + \
              experimento['iperf_src'] + \
              "-" + \
              experimento['iperf_dst'] + \
              ".log"

    hosts_iperf[1].cmd('echo >', outfile)
    # Iperf server (Se redirecciona solo la salida)
    hosts_iperf[1].cmdPrint('iperf', '-s', '-i', '1',
                            '>', outfile,
                            '&')
    hosts_iperf[0].cmdPrint('iperf', '-c', str(hosts_iperf[1].IP()), '-t ' + str(test_time) + " &")
    sleep(test_time)
    net.pingAll()
    net.stop()


def testBW_ataque(test_time, experimento):
    topo = TopoTest()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    hosts_iperf = [net.get(experimento['iperf_src']), net.get(experimento['iperf_dst'])]
    a_list = experimento['atacantes'].split("-")
    atacantes = []
    victima = net.get(experimento['victima'])
    for a in a_list:
        atacantes.append(net.get(a))

    # Archivo de salida para el iperf
    outfile = "iperf_" + \
              experimento['iperf_src'] + \
              "-" + \
              experimento['iperf_dst'] + \
              ".log"

    # Redireccion para vaciar el archivo

    hosts_iperf[1].cmd('echo >', outfile)


    # Iperf server (Se redirecciona solo la salida)
    hosts_iperf[1].cmdPrint('iperf', '-s', '-i', '1',
                            '>', outfile,
                            '&')

    # Iperf_client
    hosts_iperf[0].cmdPrint('iperf', '-c', str(hosts_iperf[1].IP()), '-t ' + str(test_time) + " &")

    # Lanzando el ataque
    info("*** Lanzado ataques...")
    for a in atacantes:
        a.cmdPrint('hping3 --flood --rand-source', str(victima.IP()), " &")
        # a.cmdPrint('ping -c 4', str(victima.IP()), " &")
        # a.cmdPrint('hping3 --flood', str(victima.IP()), " &")
        # a.cmdPrint('hping3 --rand-source', str(victima.IP()), "&")

    sleep(test_time)
    net.stop()


if __name__ == '__main__':
    print ("Empezando el ensayo")
    setLogLevel('info')
    experimento1 = {'iperf_src': 'h1','iperf_dst': 'h8'}
    experimento2 = {'iperf_src': 'h1','iperf_dst': 'h8', 'victima':'h5' , 'atacantes':'h2'}
    # test_ping()
    # testBW(50, experimento1)
    testBW_ataque(50,experimento2)

    print ("Hasta la vista baby")


