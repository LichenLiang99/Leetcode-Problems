class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #brute force TLE
#         l = 0
#         r = k
#         maxx = []
#         while r < len(nums) + 1:
#             temp = nums[l : r]
#             maxx.append(max(temp))
#             l += 1
#             r += 1
        
#         return maxx
        res = []
    
        #contain index
        q = collections.deque() 
        l = 0
        r = 0
        while r < len(nums):
            #when q is not empty and right most in q is less than current number
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            
            q.append(r)
            
            #remove left value from window
            if l > q[0]:
                q.popleft()
            
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res