# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        def Inorder(root):
            if not root:
                return 

            Inorder(root.left)
            
            #prev is initially a node, after 1st iteration it changes type to int
            if self.prev is not None:
                self.minimum = min(self.minimum, root.val - self.prev)
            self.prev = root.val
            Inorder(root.right)    

            
        self.minimum = float('inf')
        self.prev = None
        Inorder(root)
        return self.minimum
            