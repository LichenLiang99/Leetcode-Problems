# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)
            
            currmax = root.val + leftmax + rightmax
            res = max(res, currmax)
            
            return root.val + max(leftmax, rightmax)
        
        dfs(root)
        return res