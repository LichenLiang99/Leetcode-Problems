class Solution:
    def longestPalindrome(self, s: str) -> int:
        ht = defaultdict(int)
        
        for i in s:
            ht[i] += 1
            
        length = 0
        odd = 0
        
        for i in ht:
            #if we have the count as odd number, it must be in the middle
            #add to length later
            if ht[i] % 2 == 1:
                odd = 1
            #i.e if ht[1] = 5, we can still use 4 of them
            length += ht[i] // 2
        
        #fit one odd into the middle so length + 1 or + 0
        length = length * 2 + odd
        
        #if length is 0 (no even numbers exist), still check if we can fit a single odd number
        return length if length > 0 else (odd if odd > 0 else 0)
    
        #time o(n) space o(n) concept hashtable, string, math