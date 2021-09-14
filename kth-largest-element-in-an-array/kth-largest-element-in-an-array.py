class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #O(nlogn)
        # nums.sort()
        # n = len(nums)
        # return nums[n-k]
    
        #O(nlogK)
        #maintain a minheap of only size k, delete the smallest evertime heap size exceeds k
        #the 1st value of k sized minheap will be the kth largest
        pq = []
        
        for num in nums:
            heapq.heappush(pq, num)
            
            if len(pq) > k:
                heapq.heappop(pq)
            
        return pq[0]