# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(r, left, right):
            if not r:
                return True
            
            if not(r.val > left and r.val < right):
                return False
            
            return helper(r.left, left, r.val) and helper(r.right, r.val, right)
        
        return helper(root, float("-inf"), float("inf"))