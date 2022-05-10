class Solution:
    def kthSmallest(self, lists: List[List[int]], k: int) -> int:
        rows = len(lists)
        cols = len(lists[0])
        minHeap = [] #num, r, c

        for r in range(min(k, rows)):
            heappush(minHeap, (lists[r][0], r, 0))

        res = -1
        for i in range(k):
            res, r, c = heappop(minHeap)
            if c + 1 < cols:
                heappush(minHeap, (lists[r][c+1], r, c+1))

        return res