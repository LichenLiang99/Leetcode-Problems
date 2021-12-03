class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        need = 0
        for i in sorted(nums):
            res += max(need-i, 0)
            need = max(need+1, i+1)
        return res