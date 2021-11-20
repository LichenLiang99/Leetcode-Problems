class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        
        res = []
        for i in intervals:
            
            #if res is empty or start of the next is greater than end of the last interval in res (no overlap)
            if not res or res[-1][-1] < i[0]:
                res.append(i)
                
            #update the end of the last interval in res
            else:
                res[-1][1] = max(res[-1][1], i[1])
                
        return res
        
        #time 0(nlogn) space o(n)