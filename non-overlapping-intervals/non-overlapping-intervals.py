class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        end = float('-inf')
        intervals = sorted(intervals, key = lambda x:x[1])
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                res += 1
        return res