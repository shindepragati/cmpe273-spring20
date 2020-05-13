from collections import OrderedDict

hashdict = {}
item_list = []

class LRUCacheItem(object):
    """Data structure of items stored in cache"""
    def __init__(self, key, item):
        self.key = key
        self.item = item

class LRUCache(object):
    """A sample class that implements LRU algorithm"""
    def __init__(self, length):
        self.length = length
        #self.hash = {}
        #self.item_list = []
    
    def insertItem(self, item):
        """Insert new items to cache"""
        if item.key in hashdict:
            if(item in item_list):
                print(item_list)
                # Move the existing item to the head of item_list.
                item_index = item_list.index(item)
                item_list[:] = item_list[:item_index] + item_list[item_index+1:]
                item_list.insert(0, item)
        else:
            # Remove the last item if the length of cache exceeds the upper bound.
            if len(item_list) >= self.length:
                self.removeItem(item_list[-1]) #delete
            # If this is a new item, just append it to
            # the front of item_list.
            hashdict[item.key] = item
            item_list.insert(0, item) #put
        #print(f"Cache-->Number of Users={self.item_list}\nNumber of Users Cached={len(hash)}")
       
    def get(self):    
        print(hashdict) 
        return hashdict  

    def removeItem(self, item):
        """Remove those invalid items"""
        del hashdict[item.key]
        del item_list[item_list.index(item)]
        #print(f"Cache-->Number of Users={len(self.item_list)}\nNumber of Users Cached={len(hash)}")


    def remove(self, k):
        """Remove those invalid items"""
        print(k)
        if k in hashdict:
            item=hashdict[k]
            del hashdict[item.key]
            item_index = item_list.index(item)
            del item_list[item_index]
            return True
        #print(f"Cache-->Number of Users={len(item_list)}\nNumber of Users Cached={len(hash)}")


