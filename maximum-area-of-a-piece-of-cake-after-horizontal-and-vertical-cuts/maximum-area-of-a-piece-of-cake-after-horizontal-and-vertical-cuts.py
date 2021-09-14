class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        #sort both arrays first, then find max distance between 2 consecutive number
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        #initialize boundary
        max_hor = max(horizontalCuts[0], h - horizontalCuts[-1])
        max_ver = max(verticalCuts[0], w - verticalCuts[-1])
        
        #distance between two consecutive cuts
        for i in range(1, len(horizontalCuts)):
            max_hor = max(max_hor, horizontalCuts[i] - horizontalCuts[i - 1])
        
        for i in range(1, len(verticalCuts)):
            max_ver = max(max_ver, verticalCuts[i] - verticalCuts[i - 1])
            
        return (max_hor * max_ver) % (10 ** 9 + 7)
            