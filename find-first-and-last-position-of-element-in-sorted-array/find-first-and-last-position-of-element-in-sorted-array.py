class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = self.bsearch(nums, target, True)
        right = self.bsearch(nums, target, False)
        
        #since index is returned so -1 by default
        return [left, right]
        
    #LeftBias is true if we are searching left portion of the list after mid hits target
    #false if searching right portion
    def bsearch(self, nums, target, LeftBias):
        l = 0
        r = len(nums) - 1
        index = -1
        while l <= r:
            m = l + (r - l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                index = m
                if LeftBias:
                    r = m - 1
                else:
                    l = m + 1

        return index
        
        
        