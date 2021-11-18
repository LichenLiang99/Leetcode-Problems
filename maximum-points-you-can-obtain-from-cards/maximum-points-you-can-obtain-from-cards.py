class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #Start from whole right end and end at whole left end
        #sliding window
        pointer = len(cardPoints) - k
        curr = sum(cardPoints[pointer:])
        res = curr
        
        for i in range(0, k):
            curr += cardPoints[i]
            curr -= cardPoints[i+pointer]
            res = max(res, curr)
        
        return res
    
    #time o(n) space o(1)