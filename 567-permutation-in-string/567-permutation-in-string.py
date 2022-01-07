class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = [0] * 26
        l2 = [0] * 26
        
        for c in s1:
            l1[ord(c) - ord('a')] += 1
            
        for i, c in enumerate(s2):
            l2[ord(c) - ord('a')] += 1
            
            if i >= len(s1):
                l2[ord(s2[i-len(s1)]) - ord('a')] -= 1
                
            if l1 == l2:
                return True
        
        return False