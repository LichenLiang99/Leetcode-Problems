class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)), reverse = True)
        print(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[2]