class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        res = 0
        for i in nums:
            res += (i - m)
        return res