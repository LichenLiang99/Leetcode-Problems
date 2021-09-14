class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #loop with j, if j is not 0, swap with i, and increase i
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1