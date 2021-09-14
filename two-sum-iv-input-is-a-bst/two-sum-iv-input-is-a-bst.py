# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hs = set()
        return self.inorderdfs(root, hs, k)
    
    def inorderdfs(self, root, hs, k):
        if not root:
            return 
        
        complement = k - root.val
        if complement in hs:
            return True
        
        hs.add(root.val)
        
        return self.inorderdfs(root.left, hs, k) or self.inorderdfs(root.right, hs, k)
    
    #time o(n) space o(n) 