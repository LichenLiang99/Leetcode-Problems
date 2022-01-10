class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashtable = defaultdict(int)
#         for i in nums:
#             hashtable[i] += 1
        
#         for i in hashtable:
#             if hashtable[i] == 1:
#                 return i
        
#         for i in nums:
#             hashtable[i] += 1
#             if hashtable[i] == 2:
#                 del hashtable[i]
                
#         key = list(hashtable.keys())[0]
#         return key
    
#         xor
        res = 0
        for n in nums:
            res ^= n
        return res