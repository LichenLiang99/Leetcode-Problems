class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        longest = max(strs)
        shortest = min(strs)
        
        res = ""
        for i, c in enumerate(shortest):
            if longest[i] != c:
                return res
            else:
                res += c
        
        return res