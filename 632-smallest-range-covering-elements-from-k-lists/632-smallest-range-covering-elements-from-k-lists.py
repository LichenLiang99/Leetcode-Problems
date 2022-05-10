class Solution:
    def smallestRange(self, lists: List[List[int]]) -> List[int]:
        start = 0
        end = float('inf')
        maxNum = float('-inf')
        minHeap = [] #num, idx, list

        for ls in lists:
            heappush(minHeap, (ls[0], 0, ls))
            maxNum = max(maxNum, ls[0])
  
        while len(minHeap) == len(lists):
            num, idx, ls = heappop(minHeap)
            if end - start > maxNum - num:
                start = num
                end = maxNum

            if idx + 1 < len(ls):
                heappush(minHeap, (ls[idx + 1], idx + 1, ls))
                maxNum = max(maxNum, ls[idx + 1])

        return [start, end]