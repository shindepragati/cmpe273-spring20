import hashlib
import json
from server_config import NODES
import mmh3
import math
import socket
import struct

def converttolong(self,porthost):
    porthost=str(porthost)
    converted = socket.inet_aton(porthost)
    return struct.unpack("!L", converted)[0]

def calculateweight(self,node, key):
    a = 1103515245
    b = 12345
    hash = murmur(key.encode())
    return (a * ((a * node + b) ^ hash) + b) % (2^31)

def murmur(key):
    return mmh3.hash(key)


class NodeRing():

    def __init__(self, nodes):
        assert len(nodes) > 0
        self.nodes = nodes
    
    def md5(self,key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def get_node1(self, key_hex): 
        nodeslist = []
        weightlist = []
        for node in self.nodes:
            n = converttolong(self,node.port)
            n1 = converttolong(self,node.host)
            w = calculateweight(self,n+n1, key_hex)
            nodeslist.append(node)
            weightlist.append(w)
        wmax=weightlist.index(max(weightlist))
        node=nodeslist[wmax]
        return n

    def get_node(self, key):
        high_score = -1
        winner = None
        for node in self.nodes:
            score = self.md5("%s-%s" % (str(node), str(key)))
            if score > high_score:
                high_score, winner = score, node

            elif score == high_score:
                high_score, winner = score, max(str(node), str(winner))
        return winner

def test():
    ring = NodeRing(nodes=NODES)
    node = ring.get_node('9ad5794ec94345c4873c4e591788743a')
    print(node)
    print(ring.get_node('ed9440c442632621b608521b3f2650b8'))


# Uncomment to run the above local test via: python3 node_ring.py
#test()
