class Solution:
    def sortString(self, s: str) -> str:
        counter = collections.Counter(s)
        res = []
        ascending = True
        
        #for character in sorted counter, add to res and decrease the count of that character.
        #if count = 0, remove it from dictionary
        #then reverse the counter dictionary
        while counter:
            for c in sorted(counter) if ascending else reversed(sorted(counter)):
                res.append(c)
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]
            
            ascending = not ascending
        
        return ''.join(res)
    
    #time o(n) space o(n) concept hashmap, string