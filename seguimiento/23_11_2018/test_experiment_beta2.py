import csv
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

def getConfigAttriburtes(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ";")
        line_count = 0
        experimentos = []
        for row in csv_reader:
            experimentos.append(row)
    return experimentos


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


def monitorFiles( outfiles, seconds, timeoutms ):
    "Monitor set of files and return [(host, line)...]"
    devnull = open( '/dev/null', 'w' )
    tails, fdToFile, fdToHost = {}, {}, {}
    for h, outfile in outfiles.items():
        tail = Popen( [ 'tail', '-f', outfile ],
                      stdout=PIPE, stderr=devnull )
        fd = tail.stdout.fileno()
        tails[ h ] = tail
        fdToFile[ fd ] = tail.stdout
        fdToHost[ fd ] = h
    # Prepare to poll output files
    readable = poll()
    for t in tails.values():
        readable.register( t.stdout.fileno(), POLLIN )
    # Run until a set number of seconds have elapsed
    endTime = time() + seconds
    while time() < endTime:
        fdlist = readable.poll(timeoutms)
        if fdlist:
            for fd, _flags in fdlist:
                f = fdToFile[ fd ]
                host = fdToHost[ fd ]
                # Wait for a line of output
                line = f.readline().strip()
                #yield host, decode( line )
        else:
            # If we timed out, return nothing
            yield None, ''
    for t in tails.values():
        t.terminate()
    devnull.close()  # Not really necessary



def medirBW(tiempo_test, config_experiments):
    num = 0
    for experimento in config_experiments:
        num += 1
        topo = TopoTest()
        net = Mininet(topo=topo, link=TCLink)
        net.start()
        hosts_iperf = [net.get(experimento['iperf_src']), net.get(experimento['iperf_dst'])]


        # Create and/or erase output files
        if (experimento['atacantes'] == None) & (experimento['victima'] == None):
            outfiles, errfiles = {}, {}

            # Sin ataque
            outfiles[experimento['iperf_dst']] = str(num) + "_" + experimento['iperf_dst'] + ".log"
            print("Generando archivo log: " + outfiles[experimento['iperf_dst']])
            errfiles[experimento['iperf_dst']] = str(num) + "_" + experimento['iperf_dst'] + ".err"
            print("Generando archivo err: " + errfiles[experimento['iperf_dst']])

            # Iperf server
            hosts_iperf[1].cmd('echo >', experimento['iperf_dst'])
            hosts_iperf[1].cmd('echo >', experimento['iperf_dst'])
            hosts_iperf[1].cmdPrint('iperf', '-s', '-i', '1',
                                    '>', outfiles[experimento['iperf_dst']],
                                    '2>', errfiles[experimento['iperf_dst']],
                                    '&')

            # Iperf client
            #outfiles[experimento['iperf_src']] = '%s.out' % experimento['iperf_src']
            #errfiles[experimento['iperf_src']] = '%s.err' % experimento['iperf_src']
            #hosts_iperf[0].cmd('echo >', outfiles[experimento['iperf_src']])
            #hosts_iperf[0].cmd('echo >', errfiles[experimento['iperf_src']])
            # Start iperf server

            #hosts_iperf[0].cmdPrint('iperf', '-c', str(hosts_iperf[1].IP()), '-t ' + str(tiempo_test),
            #                        '>', outfiles[experimento['iperf_src']],
            #                        '2>', errfiles[experimento['iperf_src']],
            #                        '&')
            hosts_iperf[0].cmdPrint('iperf', '-c', str(hosts_iperf[1].IP()), '-t ' + str(tiempo_test) + " &")
            info("Monitoring output for", str(tiempo_test), "seconds\n")
            for h, line in monitorFiles(outfiles, tiempo_test, timeoutms=20):
                if h:
                    info('%s: %s\n' % (h.name, line))
            for h in hosts_iperf:
                h.cmd('kill %iperf')

            net.stop()


        else:
            # Con ataque
            outfiles, errfiles = {}, {}
            hosts_victima = net.get(experimento['victima'])
            lista_host_atacantes = experimento['atacantes'].split(',')
            host_atacantes = []
            for h in lista_host_atacantes:
                host_atacantes.append(net.get(h))


            #

            outfiles[experimento['iperf_dst']] = str(num) + "_" + \
                                                 experimento['iperf_dst'] + \
                                                 experimento['atacantes'] + ".log"
            errfiles[experimento['iperf_dst']] = str(num) + "_" + \
                                                 experimento['iperf_dst'] + \
                                                 experimento['atacantes'].replace(",","-") + ".err"

            # Iperf server
            hosts_iperf[1].cmd('echo >', experimento['iperf_dst'])
            hosts_iperf[1].cmd('echo >', experimento['iperf_dst'])
            hosts_iperf[1].cmdPrint('iperf', '-s', '-i', '1',
                                    '>', outfiles[experimento['iperf_dst']],
                                    '2>', errfiles[experimento['iperf_dst']],
                                    '&')

            # Iperf client
            outfiles[experimento['iperf_src']] = '%s.out' % experimento['iperf_src']
            errfiles[experimento['iperf_src']] = '%s.err' % experimento['iperf_src']
            # hosts_iperf[0].cmd('echo >', outfiles[experimento['iperf_src']])
            # hosts_iperf[0].cmd('echo >', errfiles[experimento['iperf_src']])
            # Start iperf server

            # hosts_iperf[0].cmdPrint('iperf', '-c', str(hosts_iperf[1].IP()), '-t ' + str(tiempo_test),
            #                        '>', outfiles[experimento['iperf_src']],
            #                        '2>', errfiles[experimento['iperf_src']],
            #                        '&')

            hosts_iperf[0].cmdPrint('iperf', '-c', str(hosts_iperf[1].IP()), '-t ' + str(tiempo_test), " &")

            # Lanzando los ataques a la victima


            print ("Lanzando los ataques...")
            for h in host_atacantes:
                h.cmd('hping3 --flood --rand-source', str(hosts_victima.IP()), " &")

            info("Monitoring output for", str(tiempo_test), "seconds\n")
            for h, line in monitorFiles(outfiles, tiempo_test, timeoutms=20):
                if h:
                    info('%s: %s\n' % (h.name, line))
            sleep(10)

            for h in hosts_iperf:
                h.cmd('kill %iperf')

            for h in host_atacantes:
                h.cmd('kill %hping3')

            net.stop()



if __name__ == '__main__':
    setLogLevel('info')
    experimentos = getConfigAttriburtes("test_confi1.csv")
    """
    print(experimentos)
    print(experimentos[0].keys())
    print(experimentos[0].values())
    for e in experimentos:
        print(e['iperf_src'] + '  ' + e['iperf_dst'])

    """

    medirBW(20, experimentos)
    """
    if len(sys.argv) == 1:
        print ("Uso: ...")
        # Test
    elif len(sys.argv) == 2:
        print ("Argumento %s",sys.argv[1])
    elif len(sys.argv) == 3:
        for i in range(1,len(sys.argv)):
            print("arg[%d]: %s"%(i,sys.argv[i]))
    else:
        print ("Opcion invalida")
    """


