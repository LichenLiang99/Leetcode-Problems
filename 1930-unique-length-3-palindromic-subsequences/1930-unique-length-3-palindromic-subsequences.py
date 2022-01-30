class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for letter in string.ascii_lowercase:
            l = s.find(letter)
            r = s.rfind(letter)
            if l > -1:
                res += len(set(s[l+1:r]))
        
        return res