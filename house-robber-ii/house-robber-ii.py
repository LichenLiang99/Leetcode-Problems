class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #the code below skipping first and last would not work
        #if there is only one house
        if len(nums) == 1:
            return nums[0]
    
    #since we cannot rob both 1st and last house together, we call the helper function twice
    #skipping the first and last house
    
        return max(self.robberI(nums[1:]), self.robberI(nums[:-1]))
    
    #code from Leetcode# 198 House robber I as helper function
    def robberI(self, nums):   
        rob1, rob2 = 0, 0
        
        #slide rob1 and rob2 to the right and check which is higher
        #both rob1 and rob2 is the sum of previous nums, so either rob1+current or rob2
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
    
    #time o(n) space o(1) concept dynamic programming