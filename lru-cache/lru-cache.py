#use double linked list and hashmap
class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        #hashmap
        self.cache = {}
        
        #head and tail to make add and remove easier
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    
    #double linked list remove
    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    #insert to space before tail
    #each insert is MRU
    def insert(self, node):
        p = self.tail.prev
        n = self.tail
        
        p.next = node
        node.prev = p
        n.prev = node
        node.next = n
        
    
    def get(self, key: int) -> int:
        
        #if key is in the cache, remove and insert makes it MRU and return its value
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    
        
        

    def put(self, key: int, value: int) -> None:
        
        #if already in cache, remove it(make it MRU anyways)
        if key in self.cache:
            self.remove(self.cache[key])
        
        #update key and or value, make it MRU
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
    
        #if capacity reached, get the one right after head(LRU)
        #remove from hashmap and cache
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)