class Solution:
    def sortColors(self, nums: List[int]) -> None:

        p1 = 0
        curr = 0
        p2 = len(nums) - 1
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[p1], nums[curr] = nums[curr], nums[p1]
                curr += 1
                p1 += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1
                
        #time o(n), space o(1), concept 3 pointers, sort