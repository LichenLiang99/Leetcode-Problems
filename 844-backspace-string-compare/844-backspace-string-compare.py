class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        backSpaceS = backSpaceT = 0
        
        while True:
            
            while i >= 0:
                if s[i] == '#':
                    backSpaceS += 1
                elif backSpaceS > 0:
                    backSpaceS -= 1
                else:
                    break
                i -= 1
            
            while j >= 0:
                if t[j] == '#':
                    backSpaceT += 1
                elif backSpaceT > 0:
                    backSpaceT -= 1
                else:
                    break  
                j -= 1
            
            if (i < 0 or j < 0 or (s[i] != t[j])):
                break
            
            i = i - 1
            j = j - 1
        
        return i<0 and j<0
            
    