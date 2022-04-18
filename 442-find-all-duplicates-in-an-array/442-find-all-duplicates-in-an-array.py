class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
#         hashtable = defaultdict(int)
#         res = []
#         for i in nums:
#             hashtable[i] += 1
#             if hashtable[i] > 1:
#                 res.append(i)
        
#         return res
#         res = []
#         for i in range(len(nums)):
#             ind = abs(nums[i]) - 1
#             if nums[ind] < 0:
#                 res.append(ind + 1)
#             else:
#                 nums[ind] *= -1
        
#         return res

        duplicateNumbers = []
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicateNumbers.append(nums[i])

        return duplicateNumbers