class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        
        def backtrack(first = 0):
            if first == len(nums):
                res.append(nums[:])
            
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                
                backtrack(first+1)
                
                nums[first], nums[i] = nums[i], nums[first]
        
        
        backtrack()
        return res