class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        res = 0
        maxLetterCount = 0
        freq = {}
        
        for end in range(len(s)):
            rightChar = s[end]
            if rightChar not in freq:
                freq[rightChar] = 0
            freq[rightChar] += 1
            maxLetterCount = max(maxLetterCount, freq[rightChar])
            
            if (end - start + 1 - maxLetterCount) > k:
                leftChar = s[start]
                freq[leftChar] -= 1
                start += 1
            
            res = max(res, end - start + 1)
            
        return res
            