class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        
        for num in nums:
            #check if its previous is in the set
            #if previous not in set, we have a new streak
            if num - 1 not in nums:
                curr = num
                currStreak = 1
                
                #start from current, count how many are in its streak
                while curr + 1 in nums:
                    curr += 1
                    currStreak += 1
                
                longest = max(longest, currStreak)
        
        return longest
                    
        #time o(n) space o(n) concept array, hashset