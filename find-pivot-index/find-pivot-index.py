class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = sum(nums)
        
        for index, num in enumerate(nums):
            rightsum -= nums[index]
            if rightsum == leftsum:
                return index
            leftsum += nums[index]
        
        return -1
    
    #time o(n) space o(1)