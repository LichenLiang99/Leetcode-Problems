class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ''
        
        ss = set()
        for i, c in enumerate(s):
            if c.swapcase() not in s:
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s