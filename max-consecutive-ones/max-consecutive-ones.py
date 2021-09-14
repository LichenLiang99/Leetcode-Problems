class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        curr = 0
        for n in nums:
            if n != 1:
                curr = 0
            else:
                curr += 1
                maxx = max(maxx, curr)
        
        return maxx
    
    #time o(n) space o(1) concept array