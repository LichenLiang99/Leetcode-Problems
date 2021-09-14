# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def trim(root):
            if not root:
                return None
            
            #if value > upper bound, return left brach, automatically abandon right branch
            elif root.val > high:
                return trim(root.left)
            #same for left
            elif root.val < low:
                return trim(root.right)
            #otherwise, in boundary, do regular dfs
            else:
                root.left = trim(root.left)
                root.right = trim(root.right)
                
            return root
        
        return trim(root)
    
    #time o(n) space o(n)