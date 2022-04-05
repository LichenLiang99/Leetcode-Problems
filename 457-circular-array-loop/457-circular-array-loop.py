class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        def findNext(forward, currIndex):
            direction = nums[currIndex] >= 0
            if direction != forward:
                return -1
            
            nextIndex = (nums[currIndex] + currIndex) % len(nums)
            if nextIndex == currIndex:
                return -1
            
            return nextIndex
        
        
        for i, n in enumerate(nums):
            forward = n >= 0
            slow = i
            fast = i
            
            while True:
                slow = findNext(forward, slow)
                fast = findNext(forward,fast)
                if fast != -1:
                    fast = findNext(forward,fast)
                
                if slow == -1 or fast == -1 or slow == fast:
                    break
                
            if slow != -1 and slow == fast:
                return True
        
        return False