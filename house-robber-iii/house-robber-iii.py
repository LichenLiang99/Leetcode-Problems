# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        return max(self.dfs(root))
    
    #return pair [withRoot, withoutRoot]
    def dfs(self, root):
        if not root:
            return [0, 0]
        
        leftPair = self.dfs(root.left)
        rightPair = self.dfs(root.right)
        
        #withRoot: sum of current root value with withoutRoot of both childs
        withRoot = root.val + leftPair[1] + rightPair[1]
        
        #withoutRoot: sum maximum of both childs
        #for this, we can either take with or without root of its child
        withoutRoot = max(leftPair) + max(rightPair)
        
        return [withRoot, withoutRoot]
    
    #time o(n) space o(1) concept tree, dynamic programming