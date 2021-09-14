class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            
            mid = l + (r - l) // 2
            
            #make sure mid is even on the left
            if mid % 2 == 1:
                mid -= 1
                
            #all numbers start on an even index and end in an odd index,
            #until it hits single number
            #so if current even index value is same as its next, means single value is at right portion of the array
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        
        return nums[l]
    
    #time o(logn) space o(1)