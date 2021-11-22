class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        i = len(nums) - 1
        j = len(nums) - 1
        
        #find decreasing part
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        #if nums is decreasing, reverse it
        if i == 0:
            nums.reverse()
            return
        
        #pivot
        k = i - 1
        
        #find rightmost successor to pivot
        while nums[j] <= nums[k]:
            j -= 1
        
        #swap pivot
        nums[j], nums[k] = nums[k], nums[j]
        
        #reverse rest of the decreasing part
        l = k + 1
        r = len(nums) - 1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        