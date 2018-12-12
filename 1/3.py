from mininet.mininet.cli import CLI
from mininet.mininet.link import Link
from mininet.mininet.net import Mininet
from mininet.mininet.node import RemoteController
from mininet.mininet.term import makeTerm

if '__main__' == __name__:

    net = Mininet(controller=RemoteController)
    