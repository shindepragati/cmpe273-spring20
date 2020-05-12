import hashlib
from server_config import NODES

class NodeRing(object):
 
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.allring = dict()
        self.sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)
    
    def add_node(self, node):
        for i in range(0, self.replicas):
            key = self.keygenerator('%s:%s' % (node, i))
            self.allring[key] = node
            self.sorted_keys.append(key)
        self.sorted_keys.sort()
    
    def get_node(self, key):
        val = self.find_node_position(key)[0]
        return val
    
    def find_node_position(self, key):
        key = self.keygenerator(key)
        nodes = self.sorted_keys
        for i in range(0, len(nodes)):
            node = nodes[i]
            if key <= node:
                return self.allring[node], i
        return self.allring[nodes[0]], 0
    
    def get_nodes(self, string_key):
        print("get node")
        node, position = self.find_node_position(string_key)
        for key in self.sorted_keys[position:]:
            yield self.allring[key]   #return the value but msintsin the state
        while True:
            for key in self.sorted_keys:
                yield self.allring[key]
    
    def keygenerator(self, key):
        h = hashlib.md5()
        h.update(key.encode('utf-8'))
        return int(h.hexdigest(), 16)

def test():
    ring = NodeRing(nodes=NODES)
    node = ring.get_nodes('9ad5794ec94345c4873c4e591788743a')
    print(node)
    print(ring.get_nodes('ed9440c442632621b608521b3f2650b8'))

#test()