class ListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.ht = [None] * self.size 
        

    def put(self, key: int, value: int) -> None:
        
        index = key % self.size
        
        if self.ht[index] == None:
            self.ht[index] = ListNode(key, value)
        else:
            curr = self.ht[index]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if not curr.next:
                    break
                
                curr = curr.next
            curr.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        index = key % self.size
        curr = self.ht[index]
        while curr:
            if curr.key == key:
                return curr.value
            else:
                curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        index = key % self.size
        curr = prev = self.ht[index]
        if not curr:
            return
        
        if curr.key == key:
            self.ht[index] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key != key:
                    prev = prev.next
                    curr = curr.next
                else:
                    prev.next = curr.next
                    return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)