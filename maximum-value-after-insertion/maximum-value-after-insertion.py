class Solution:
    def maxValue(self, s: str, x: int) -> str:
        if s[0] != '-':
            i = 0
            while i < len(s) and x <= int(s[i]):
                i += 1
        else:
            i = 1
            while i < len(s) and x >= int(s[i]):
                i += 1
                
        return s[:i] + str(x) + s[i:]
        