class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        msum = sum(rolls)
        total = (n + m) * mean
        
        nsum = total - msum
        
        if nsum < n or nsum > 6*n:
            return []
        
        res = []
        while nsum:
            dice = min(nsum-n+1, 6)
            res.append(dice)
            nsum -= dice
            n -= 1
        
        return res
        
        