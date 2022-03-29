class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        
        res = 0
        
        for i in range(len(nums)):
            count = 0
            
            #change nums[i] to -1 meaning it's visited
            while nums[i] != -1:
                nums[i], i, count = -1, nums[i], count + 1
                
            #return largest count
            res = max(res, count)
        
        return res
        
        #time o(n) space o(1)