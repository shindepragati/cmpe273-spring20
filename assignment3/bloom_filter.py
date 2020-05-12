import math 
import mmh3 
from bitarray import bitarray 
from sample_data import USERS
from pickle_hash import serialize_GET, serialize_PUT, serialize_DELETE
from random import shuffle 

n = 10 #no of items to add 
p = 0.05 #false positive probability 

class BloomFilter(object): 
   
    @classmethod
    def __init__(self, items_count,fp_prob): 
        self.fp_prob = fp_prob 
  
        self.size = self.get_size(items_count,fp_prob) 
  
        self.hash_count = self.get_hash_count(self.size,items_count) 
  
        self.bit_array = bitarray(self.size) 
  
        self.bit_array.setall(0) 
  
    @classmethod
    def add(self, item): 
        digests = [] 
        for i in range(self.hash_count): 
            digest = mmh3.hash(item,i) % self.size 
            digests.append(digest) 
  
            self.bit_array[digest] = True
  
    @classmethod
    def is_member(self, item): 
        for i in range(self.hash_count): 
            digest = mmh3.hash(item,i) % self.size 
            if self.bit_array[digest] == False: 
  
                # if any of bit is False then,its not present 
                # in filter 
                # else there is probability that it exist 
                return False
        return True
  
    @classmethod
    def get_size(self,n,p): 
        m = -(n * math.log(p))/(math.log(2)**2) 
        return int(m) 
  
    @classmethod
    def get_hash_count(self, m, n): 
        k = (m/n) * math.log(2) 
        return int(k) 
