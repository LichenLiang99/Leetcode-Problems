class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textCount = Counter(text)
        balloonCount = Counter("balloon")
        
        res = len(text)
        for c in balloonCount:
            res = min(res, textCount[c] // balloonCount[c])
        
        return res