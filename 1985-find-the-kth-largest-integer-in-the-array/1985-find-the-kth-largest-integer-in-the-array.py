class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxheap = [-int(n) for n in nums]
        
        heapq.heapify(maxheap)
        
        while k > 1:
            heapq.heappop(maxheap)
            k -= 1
        
        return str(-maxheap[0])