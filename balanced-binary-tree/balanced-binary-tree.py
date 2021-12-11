# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
#         #the returned height must not be -1
#         return True if self.getHeight(root) >= 0 else 0
    
#     #recursively calculate the height
#     def getHeight(self, root):
        
#         if root is None:
#             return 0
        
#         #if one of them is -1, means the tree is unbalanced below, then pass -1 to the root to return false
#         left, right = self.getHeight(root.left), self.getHeight(root.right)
#         if left < 0 or right < 0 or abs(left - right) > 1:
#             return -1
#         else:
#             return max(left, right) + 1
        
#         #time o(n) space o(1) concept tree recursion

        def helper(r):
            if not r:
                return 0
            left = helper(r.left)
            right = helper(r.right)
            if left < 0 or right < 0 or abs(left-right) > 1:
                return -1
            else:
                return max(left, right) + 1
        
        return True if helper(root) >= 0 else False