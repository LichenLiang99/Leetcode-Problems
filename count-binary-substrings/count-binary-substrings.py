class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre, curr = 0, 1
        count = 0
        
        #count the ones that belong to the same category 0 or 1 and store in current
        #prev is the count of the previous set
        for i in range(1, len(s)):
            
            if s[i] == s[i-1]:
                curr += 1
            else:
                pre = curr
                curr = 1
            
            if pre >= curr:
                count += 1
        return count
    #time o(n) space o(1) concept string 