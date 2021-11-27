class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax = 1
        currMin = 1
        
        for n in nums:
            
            temp = currMax * n
            currMax = max(n, temp, currMin * n)
            currMin = min(n, temp, currMin * n)
            
            res = max(res, currMax)
        
        return res