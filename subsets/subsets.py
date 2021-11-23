class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(first, len(nums)):
                
                curr.append(nums[i])
                backtrack(i+1, curr)
                
                curr.pop()
        
        for k in range(len(nums)+1):
            backtrack()
        return res