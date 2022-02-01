class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #Start from whole right end and end at whole left end
        #sliding window
        pointer = len(cardPoints) - k - 1
        curr = sum(cardPoints[pointer + 1:])
        res = curr
        
        for i in range(0, k):
            curr += cardPoints[i]
            pointer += 1
            curr -= cardPoints[pointer]
            res = max(res, curr)
        
        return res
    
    #time o(n) space o(1)