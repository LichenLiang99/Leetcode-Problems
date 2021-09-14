# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minn = root.val
        self.ans = float('inf')
        
        #use the fact that a node's child is always equal or greater than itself
        def dfs(node):
            if node:
                if minn < node.val < self.ans:
                    self.ans = node.val
                else:
                    dfs(node.left)
                    dfs(node.right)
        
        dfs(root)
        return self.ans if self.ans < float('inf') else -1
    
    #time o(n) space o(n) concept tree