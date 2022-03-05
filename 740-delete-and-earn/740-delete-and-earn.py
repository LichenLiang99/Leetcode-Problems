class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ht = collections.Counter(nums)
        rob1, rob2 = 0, 0
        for value in range(10001):
            temp = max(rob1 + ht[value]*value, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
    
    #time o(n) space o(n)