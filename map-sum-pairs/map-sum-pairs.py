class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.sum = 0
    
class MapSum:

    def __init__(self):
        self.trieRoot = TrieNode()
        self.map = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map[key]
        curr = self.trieRoot
        for c in key:
            curr = curr.child[c]
            curr.sum += diff
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.trieRoot
        for c in prefix:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
        return curr.sum

    #time insert o(k) length of key, sum o(p) length of prefix, space o(T) total of nodes

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)