import sys
import socket

from node_ring import NodeRing
from sample_data import USERS
from server_config import NODES
from pickle_hash import serialize_GET, serialize_PUT, serialize_DELETE,deserialize
from lru_cache import *
from bloom_filter import BloomFilter 

BUFFER_SIZE = 1024
hash_codes = set()   
NUM_KEYS = 3
FALSE_POSITIVE_PROBABILITY = 0.05
bloomfilter = BloomFilter(NUM_KEYS, FALSE_POSITIVE_PROBABILITY) 

class UDPClient():
    def __init__(self, host, port):
        self.host = host
        self.port = int(port) 


    def send(self, request):
        #print('Connecting to server at {}:{}'.format(self.host, self.port))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(request, (self.host, self.port))
            response, ip = s.recvfrom(BUFFER_SIZE)
            return response
        except socket.error:
            print("Error! {}".format(socket.error))
            exit()
    
    @classmethod
    def put(self,udp_clients,key,data_bytes):
        # PUT all users.
        ring = NodeRing(NODES)
        fix_me_server_id = NODES.index(ring.get_node(key))
        response = udp_clients[fix_me_server_id].send(data_bytes)
        hash_codes.add(response)
        print(f"Server--->Number of Users Cached={len(hash_codes)}")
        return "hi"
   
    @classmethod
    def getAll(self,udp_clients):
        for hc in hash_codes:
            data_bytes, key = serialize_GET(hc)
            ring = NodeRing(NODES)
            fix_me_server_id = NODES.index(ring.get_node(key))
            print(data_bytes)
            response = udp_clients[fix_me_server_id].send(data_bytes)
            print(f"Server GETALL--->{response}")  
        return response

    @classmethod
    def get(self,udp_clients,key):
        k=key.encode()
        for hc in hash_codes:
            if(hc==k):
                data_bytes, key = serialize_GET(hc)      
                ring = NodeRing(NODES)
                fix_me_server_id = NODES.index(ring.get_node(key))
                response = udp_clients[fix_me_server_id].send(data_bytes)
                return response 
        return None

    @classmethod
    def delete(self,udp_clients,key): 
        k=key.encode()
        for hc in hash_codes:
            print(hash_codes)
            if(hc==k):
                data_bytes, key = serialize_DELETE(hc)      
                ring = NodeRing(NODES)
                fix_me_server_id = NODES.index(ring.get_node(key))
                response = udp_clients[fix_me_server_id].send(data_bytes)
                hash_codes.remove(hc)
                #print(hash_codes)
                break
        print(f"Server DELETE--->Number of Users Cached={len(hash_codes)}")

cclient =UDPClient

@lru_cache(3)
def get(key):
    if bloomfilter.is_member(key):
        return cclient.get(udp_client,key)
    else:
        return None 

@lru_cache(3)
def put(key, value):
    bloomfilter.add(key)
    return cclient.put(udp_client,key, value)

@lru_cache(3)
def delete(key):
    if bloomfilter.is_member(key):
        return cclient.delete(udp_client,key)
    else:
        return None


uq = UDPClient

if __name__ == "__main__":
   
    clients = [
        UDPClient(server['host'], server['port'])
        for server in NODES
    ]

    udp_client=clients    

    for u in USERS:
        data_bytes, key = serialize_PUT(u)
        put(key,data_bytes)
    

    #uq.get(clients,'1c84c3d6dec3775654c4573ca4df1064')
    #uq.getAll(clients)
    #uq.delete(clients,'1c84c3d6dec3775654c4573ca4df1064')
    #getAllData(clients)

    get('1c84c3d6dec3775654c4573ca4df1064')

    delete('1c84c3d6dec3775654c4573ca4df1064')

    get('1c84c3d6dec3775654c4573ca4df1064')