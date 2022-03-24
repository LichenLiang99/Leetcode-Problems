class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = collections.Counter(t)
        window = {}
        
        have = 0
        need = len(countT) #number of unique character in t
        res = [-1, -1]
        resLen = float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1 
                
            while have == need:
                #update result
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                #pop from left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
    
    #time o(n) space o(n)