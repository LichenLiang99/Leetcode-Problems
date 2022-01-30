class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            
        reverse(nums, 0, len(nums) - 1) #reverse whole array
        reverse(nums, 0, k-1) #reverse first half until k
        reverse(nums, k, len(nums) - 1) #reverse second half
        
        