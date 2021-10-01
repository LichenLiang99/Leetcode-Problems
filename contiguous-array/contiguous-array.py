class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapp = {0:-1} #count : index
        count = 0
        maxx = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
                
            if count in mapp:
                maxx = max(maxx, i - mapp[count])
            else:
                mapp[count] = i
        
        return maxx
    
    #time o(n) space o(n)