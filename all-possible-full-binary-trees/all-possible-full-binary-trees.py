# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        dp = {} #map n:list
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            
            res = []
            for l in range(n):
                r = n - 1 - l
                left = backtrack(l)
                right = backtrack(r)
                
                for t1 in left:
                    for t2 in right:
                        res.append(TreeNode(0, t1, t2))
            dp[n] = res    
            return res
        
        return backtrack(n)