class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {} #index : [lenLIS, count]
        lenLIS = 0
        res = 0
        
        for i in range(len(nums) - 1, -1, -1):
            maxLen = 1
            maxCnt = 1
            
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        maxLen = length + 1
                        maxCnt = count
                    elif length + 1 == maxLen:
                        maxCnt += count
            
            if maxLen > lenLIS:
                lenLIS = maxLen
                res = maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            
            dp[i] = [maxLen, maxCnt]
            
        
        return res
        