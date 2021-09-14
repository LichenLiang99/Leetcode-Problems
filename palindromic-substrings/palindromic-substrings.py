class Solution:
    def countSubstrings(self, s: str) -> int:
        
#         count = 0
        
#         for i in range(len(s)):
#             #expand to both side in odd numbers. i.e "c,a,b,a,c"
#             l = i
#             r = i
#             while l >=0 and r < len(s) and s[l] == s[r]:
#                 count += 1
#                 l -= 1
#                 r += 1
            
#             #expand to both side in even numbers.i.e "a,a,b,b,c,c"
#             l = i
#             r = i + 1
#             while l >=0 and r < len(s) and s[l] == s[r]:
#                 count += 1
#                 l -= 1
#                 r += 1
        
#         return count
    
    #time o(n2) space o(1) concept string, two pointer
    
    #cleaner version of code
        count = 0
        for i in range(len(s)):
            count += self.countP(s, i, i)
            count += self.countP(s, i, i + 1)
        return count
    
    def countP(self, s, l, r):
        res = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
