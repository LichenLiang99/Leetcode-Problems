# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return None
        
        #stop when root has not left and right branch, and the value match our sum
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        #otherwise, subtract value from sum and keep going
        targetSum -= root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
    #time o(n) space o(n) concept tree