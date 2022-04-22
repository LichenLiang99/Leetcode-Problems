class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #sum of 1..n = n(n+1) / 2
        # total = (len(nums) * (len(nums) + 1))//2
        # return total - sum(nums)
    
#         res = len(nums)
#         for i in range(len(nums)):
#             res += (i - nums[i])
        
#         return res
        nums.sort()
        l = 0
        r = len(nums)
        
        while l < r:
            m = l + (r-l) // 2
            
            if m == nums[m]:
                l = m + 1
            else:
                r = m
        
        
        return l