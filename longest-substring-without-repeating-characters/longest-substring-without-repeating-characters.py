class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        #create a set to store substring, and a left pointer
        charSet = set()
        length = 0
        l = 0
        
        #for right pointer, if at right index it's in the set, delete character at left pointer and move up l
        #i.e abcdefgf: delete a,b,c...f to leave only gf
        #then add right pointer to set and update length
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            length = max(length, r - l + 1)
            
        return length
    
        #time o(n) space o(n) concept string, sliding window
        
        
        