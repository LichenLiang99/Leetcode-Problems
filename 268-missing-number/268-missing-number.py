class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #sum of 1..n = n(n+1) / 2
        # total = (len(nums) * (len(nums) + 1))//2
        # return total - sum(nums)
    
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res