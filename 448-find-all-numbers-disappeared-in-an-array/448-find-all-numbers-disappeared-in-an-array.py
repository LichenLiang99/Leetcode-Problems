class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
#         hashtable = dict()
        
#         #for each value that exist, hash[value] = 1, and find the non existent
#         for n in nums:
#             hashtable[n] = 1
        
#         res = []
        
#         for i in range(1, len(nums) + 1):
#             if i not in hashtable:
#                 res.append(i)
        
#         return res
    
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
            
        res = []
        
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res