class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            #if current array is sorted, just return leftmost
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            #if current array is not sorted
            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            
            #if mid belongs to left portion, search the right
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            
        return res

    
    #time o(logn) space o(1) concept binary search