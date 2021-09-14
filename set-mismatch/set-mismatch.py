class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        miss = 1
        
        #for each number in nums, if its value is < 0, then it's repeted, otherwise, set the value at this index to -ve
        for i in nums:
            if nums[abs(i)-1] < 0:
                dup = abs(i)
            else:
                nums[abs(i)-1] *= -1
        
        #for each number in nums, if its value is > 0, this indexed number is missing
        for i in range(1,len(nums)+1):
            if nums[i-1] > 0:
                miss = i
                break

        
        return [dup, miss]
    
    #time o(n) space o(1)