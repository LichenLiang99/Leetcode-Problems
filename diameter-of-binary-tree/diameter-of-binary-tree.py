# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
#         dia = [0]
        
#         def dfs(root):
#             if not root:
#                 return -1
#             l = dfs(root.left)
#             r = dfs(root.right)
#             dia[0] = max(dia[0], 2 + l + r)
            
#             return 1 + max(l, r)
        
#         dfs(root)
#         return dia[0]

        diameter = 0
    
        def longestpath(root):
            if not root:
                return 0
            
            #diameter does not belong to inner function
            nonlocal diameter
            
            l = longestpath(root.left)
            r = longestpath(root.right)
            diameter = max(diameter, l + r)
            
            return max(l, r) + 1
        
        longestpath(root)
        return diameter