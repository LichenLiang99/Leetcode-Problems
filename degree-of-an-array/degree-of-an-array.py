class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        #to store the count of each value
        htcount = defaultdict(int)
        #to store the index of first occurance of this value
        htFirstOccurIndex = {}
        res = 0
        degree = 0
        
        for index, n in enumerate(nums):
            #add to hashmap
            htFirstOccurIndex.setdefault(n, index)
            htcount[n] += 1
            
            #if count larger than current degree, update degree
            if htcount[n] > degree:
                degree = htcount[n]
                res = index - htFirstOccurIndex[n] + 1
            elif htcount[n] == degree:
                res = min(res, index - htFirstOccurIndex[n] + 1)
        
        return res
    
    #time o(n) space o(n)