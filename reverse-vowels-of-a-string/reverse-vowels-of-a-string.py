class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        l = 0
        r = len(s) - 1
        s = list(s)
        
        while l < r:
            if s[l] in vowel and s[r] in vowel:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
                
            elif s[l] not in vowel:
                l += 1
            else:
                r -= 1

        
        return "".join(s)