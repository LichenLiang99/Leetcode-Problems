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
    
        for i in range(len(nums)):
            
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative 
            # thus indicating that the number nums[i] has 
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
                
        return result        