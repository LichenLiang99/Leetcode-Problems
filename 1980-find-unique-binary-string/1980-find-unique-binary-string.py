class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = {s for s in nums}
        
        def backtrack(i, curr):
            if i == len(nums):
                res = "".join(curr)
                return None if res in strSet else res
            
            res = backtrack(i+1, curr)
            if res:
                return res
            
            curr[i] = "1"
            res = backtrack(i+1, curr)
            if res:
                return res
        
        return backtrack(0, ["0" for s in nums])
 