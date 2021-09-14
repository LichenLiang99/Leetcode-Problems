# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        
        
        def dfs(node, parentVal):
            if not node:
                return 0
            
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            self.longest = max(self.longest, left + right) 
            return 1 + max(left, right) if node.val == parentVal else 0
        
        dfs(root, None)
        
        return self.longest
    
    #time o(n) space o(n) concept tree, dfs