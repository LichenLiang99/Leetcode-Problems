class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        
        def compare(x1, x2):
            if x1 + x2 > x2 + x1:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key = cmp_to_key(compare))
        
        return str(int("".join(nums)))