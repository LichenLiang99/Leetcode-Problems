class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht = defaultdict(int)
        
        #increase counter
        for i in s:
            ht[i] += 1
        
        #if not in hashtable, false, else decrese its counter
        for i in t:
            if i not in ht:
                return False
            else:
                ht[i] -= 1
              
        #make sure all entries are 0
        for i in ht:
            if ht[i] != 0:
                return False
            
        return True
    
        #time o(n) space o(n) concept string, hash table