class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        ht = defaultdict(int)
        
        for i in nums:
            ht[i] += 1
            if ht[i] > 1:
                return True
        return False
    
        