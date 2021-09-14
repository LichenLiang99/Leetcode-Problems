class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or not s or not t:
            return False
        
        ht = {}
        ht2 = {}
        s = list(s)
        t = list(t)
        
        for i in range(len(s)):
            if (s[i] in ht and ht[s[i]] != t[i]) or (t[i] in ht2 and ht2[t[i]] != s[i]):
                return False
            else:
                ht[s[i]] = t[i]
                ht2[t[i]] = s[i]
        return True
    
    #time o(n) space o(n) concept strings, hash table