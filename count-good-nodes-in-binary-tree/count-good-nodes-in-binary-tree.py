# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxx):
            
            if not node:
                return 0
            if node.val >= maxx:
                res = 1
            else:
                res = 0
                
            maxx = max(maxx,node.val)
            res += dfs(node.left, maxx)
            res += dfs(node.right, maxx)
            
            return res
        
        return dfs(root, root.val)