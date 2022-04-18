class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #hashtable method
        
#         hashtable = defaultdict(int)
        
#         for i in nums:
#             hashtable[i] += 1
            
#         for i in hashtable:
#             if hashtable[i] != 1:
#                 return i
            
        #Floyd's Cycle Detection
#         slow, fast = 0, 0

#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 break

#         slow2 = 0
#         while True:
#             slow = nums[slow]
#             slow2 = nums[slow2]
#             if slow == slow2:
#                 return slow2

        
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    return nums[i]
            else:
                i += 1
        return -1