class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
       #Moore Voting Algo
        counter = 0
        candidate = None
        
        for i in nums:
            if counter == 0:
                candidate = i
            if candidate == i:
                counter += 1
            else:
                counter -= 1
        return candidate
    
        #Sorting
        #since majority element > N/2, midvalue is majority element
        # nums.sort()
        # return nums[len(nums)//2]
    