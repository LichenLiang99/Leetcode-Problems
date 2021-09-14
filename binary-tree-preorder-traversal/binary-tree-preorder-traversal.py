# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         s = []

        
#         if root:
            
#             s.append(root.val)
#             s = s + self.preorderTraversal(root.left)
#             s = s + self.preorderTraversal(root.right)
        
#         return s
        
        s = [root]
        l = []
        
        while s:
            curr = s.pop()
            if curr:
                l.append(curr.val)
                s.append(curr.right)
                s.append(curr.left)
        
        return l