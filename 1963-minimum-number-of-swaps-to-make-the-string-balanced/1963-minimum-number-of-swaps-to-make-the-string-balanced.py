class Solution:
    def minSwaps(self, s: str) -> int:
        maxx = 0
        closing = 0
        for c in s:
            if c == "]":
                closing += 1
            else:
                closing -= 1
            
            maxx = max(maxx, closing)
        
        return (maxx + 1)//2