# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         s = []

#         if root:
            
#             s = s + self.postorderTraversal(root.left)
#             s = s + self.postorderTraversal(root.right)
#             s.append(root.val)
        
#         return s

        stack2 = []
        stack1 = [root]
        l = []
        while stack1:
            curr = stack1.pop()
            if curr:
                stack2.append(curr.val)
                stack1.append(curr.left)
                stack1.append(curr.right)
        
        while stack2:
            c = stack2.pop()
            l.append(c)
            
        return l