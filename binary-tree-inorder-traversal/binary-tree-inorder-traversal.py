# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        s = []
        curr = root
        l = []
        
        if root:
            
            s = s + self.inorderTraversal(root.left)
            s.append(root.val)
            s = s + self.inorderTraversal(root.right)
        
        return s
        
#         while curr or s:
#             while curr:
#                 s.append(curr)
#                 curr = curr.left
#             curr = s.pop()
#             l.append(curr.val)
#             curr = curr.right
        
#         return l