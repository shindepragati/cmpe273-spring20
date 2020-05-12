from pickle_hash import serialize_GET, serialize_PUT, serialize_DELETE,deserialize
from lru import LRUCacheItem,LRUCache
import functools
from sample_data import USERS
from lru import item_list
def lru_cache(size):
    #cache = {}
    #cache_keys = []
    
    def lrucache_dec(func):
        def cached_fn(*args):
            key=""
            data_bytes=""
   
            #print(func.__name__)
            cache = LRUCache(size)
            fname=func.__name__
           
            if(len(args)==1):
                key = args[0]
                #print(key)
            if(len(args)==2):
                key = args[0]
                data_bytes =args[1]
            if(fname=='put' or fname=='fibonacci'):
                temp = LRUCacheItem(key,data_bytes) 
                cache.insertItem(temp) 
                print("LRU--->Number of Users Cached="+str(len(item_list)))
                retval = func(*args)
            if(fname=='get' or fname=='get_data'):
                hashval=cache.get()
                if key in hashval:
                    item=hashval[key]
                    data_bytes, key = serialize_GET(item)
                    print("LRU Get-->")
                    print(key)
                    #print(deserialize(data_bytes))             
                else:
                    retval = func(*args) 
                    if(retval!=None):
                        print("Server Get --> Success")
                        print(key)
                        #print(deserialize(retval)) 
                    else:
                        print("Server Get-->"+key+'--->KEY NOT FOUND')     
            if(fname=='delete'):
                if(cache.remove(key)):
                    print("LRU Delete-->"+key)  
                else:
                    print("LRU Delete-->"+key+'--->KEY NOT FOUND') 
                
                retval=func(*args)
                print("Server Delete-->"+key)  
            
           
            return retval
        return cached_fn
    return lrucache_dec

if __name__ == '__main__':
    @lru_cache(5)
    def to_be_cached(foo, bar):
       print("Computing for %r, %r" % (foo, bar))
       return foo * 1000 + bar * 100
    
    print(to_be_cached(3, 5))
    print(to_be_cached(4, 5))
    print(to_be_cached(5, 5))
    print(to_be_cached(6, 5))
 