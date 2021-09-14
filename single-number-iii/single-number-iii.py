class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
#         l = []
        
#         hashtable = defaultdict(int)
#         for i in nums:
#             hashtable[i] += 1
        
#         for i in hashtable:
#             if hashtable[i] == 1:
#                 l.append(i)
        
#         return l
    
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)
        
        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num
        
        return [x, bitmask^x]