#!/usr/bin/python

"""
Simple topology

         c0
          |
          |
   h1 --- s1 --- h3
          |
          |
          h2

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.

More info: http://csie.nqu.edu.tw/smallko/sdn/lab2.htm
Use:

-> Controller: running the pox controller as a switch

   cd $HOME/pox
   ./pox.py log.level --DEBUG forwarding.l2_learning 

-> Topology:

   sudo mn --custom simple_topo_controller_mn.py --topo single3 --controller=remote,ip=127.0.0.1,port=6633

"""

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.util import irange


class SingleTopo3(Topo):
   "Single topology of 3 host connected to a single switch"
   def __init__(self):
     
      super(SingleTopo3, self).__init__() # Topo.__init__( self )
      switch = self.addSwitch('s1')
      for i in irange(1, 3):
           host = self.addHost('h%s' % i)
           self.addLink( host, switch)

           

topos = { 'single3': ( lambda: SingleTopo3() ) }

   
'''
if __name__ == '__main__':
    setLogLevel( 'info' )
    info('*** Creating the network\n')
    net = Mininet(topo=SingleSwitchTopo(3), controller=POXBridge)
    info('*** Starting network\n')
    net.start()
    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping network')
    net.stop()
'''


