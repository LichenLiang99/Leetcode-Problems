class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxx = -1
        res = 0
        
        for index, n in enumerate(arr):
            maxx = max(maxx, n)
            if maxx == index:
                res += 1
        
        return res
    
    #time o(n) space o(1)