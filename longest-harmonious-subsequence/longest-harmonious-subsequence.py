class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ht = defaultdict(int)
        for i in nums:
            ht[i] += 1
        
        maximum = 0
        for i in ht:
            if i+1 in ht:
                maximum = max(maximum, ht[i] + ht[i+1])
                
        return maximum
    
    #time o(n) space o(n) concept hashtable, 