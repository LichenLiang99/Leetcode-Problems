class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        #store index and its sum
        d = collections.deque([[0, 0]])
        res = float('inf')
        currSum = 0
        
        for index, num in enumerate(nums):
            currSum += num
            
            #while dequeue is not empty and sum - 1st sum is greater than k
            while d and currSum - d[0][1] >= k:
                res = min(res, index + 1 - d.popleft()[0])
            
            #while currSum < last sum in dequeue
            while d and currSum <= d[-1][1]:
                d.pop()
            
            d.append([index + 1, currSum])
        
        return res if res < float('inf') else -1
    
    #time o(n) space o(n)