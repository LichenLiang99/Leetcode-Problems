class Solution:
    def rob(self, nums: List[int]) -> int:
        #[rob1, rob2, n, n+1, ...]
        rob1, rob2 = 0, 0
        
        #slide rob1 and rob2 to the right and check which is higher
        #both rob1 and rob2 is the sum of previous nums, so either rob1+current or rob2
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
    
    #time o(n) space o(1) concept dynamic programming