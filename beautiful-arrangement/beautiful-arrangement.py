class Solution:
    
    
        
    def countArrangement(self, n: int) -> int:
        
        
        l = list(range(1, n+1, 1))    
        return self.count(l, 1)
    
    def count(self, l, index):
        if len(l) == 0:
            return 1
        ans = 0
        for i in range(len(l)):
            if l[i] % index == 0 or index % l[i] == 0:
                ans += self.count(l[:i] + l[i+1:], index + 1)
        return ans