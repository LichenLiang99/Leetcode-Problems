class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #using hashmap from leetcode 1
#         mapp = dict()
        
#         for i in range(len(numbers)):
#             n = numbers[i]
#             complement = target - n
#             if n in mapp:
#                 return [mapp[n] + 1, i + 1]
#             else:
#                 mapp[complement] = i
        
    
        #using two pointer 
        l = 0 
        r = len(numbers)-1
        
        while l < r: 
            if numbers[l] + numbers[r] == target: 
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target: 
                r-=1 
            elif numbers[l] + numbers[r] < target: 
                l+=1