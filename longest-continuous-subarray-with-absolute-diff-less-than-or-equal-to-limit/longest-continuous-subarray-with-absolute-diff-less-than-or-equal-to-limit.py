class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = collections.deque()
        minq = collections.deque()
        i = 0
        for n in nums:
            while maxq and n > maxq[-1]:
                maxq.pop()
            while minq and n < minq[-1]:
                minq.pop()
            
            maxq.append(n)
            minq.append(n)
            
            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[i]:
                    maxq.popleft()
                if minq[0] == nums[i]:
                    minq.popleft()
                i += 1
        
        return len(nums) - i