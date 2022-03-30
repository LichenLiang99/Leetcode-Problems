class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
#         maxSub = nums[0]
#         currSum = 0
        
#         for i in nums:
#             if currSum < 0:
#                 currSum = 0
#             currSum += i
#             maxSub = max(maxSub, currSum)
            
#         return maxSub
    
        maxSub = nums[-1]
        curr = 0
        
        for i in range(len(nums)-1, -1, -1):
            if curr < 0:
                curr = 0
            curr += nums[i]
            maxSub = max(maxSub, curr)
        
        return maxSub