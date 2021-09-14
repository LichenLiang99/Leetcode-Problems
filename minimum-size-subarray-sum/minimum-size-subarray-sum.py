class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window
        res = len(nums) + 1
        l = 0
        for r in range(len(nums)):
            target -= nums[r]
            while target <= 0:
                res = min(res, r - l + 1)
                target += nums[l]
                l += 1
                
        
            
        return res % (len(nums) + 1)