class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        mapp = dict()
        
        for i in range(len(nums)):
            n = nums[i]
            complement = target - n
            if n in mapp:
                return [mapp[n], i]
            else:
                mapp[complement] = i
            
        #time o(n) space o(n)