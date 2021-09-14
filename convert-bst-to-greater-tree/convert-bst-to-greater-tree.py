# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #recursion
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
            
        return root
    
        #iterative
#         total = 0
#         s = []
#         node = root
#         while s or node:
#             while node:
#                 s.append(node)
#                 node = node.right
            
#             node = s.pop()
#             total += node.val
#             node.val = total
            
#             node = node.left
        
#         return root
    
    #time o(n) space o(n) concept tree