# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return None
        
        #return true if root has no left and right child
        def isleaf(root):
            return root and not root.left and not root.right
        
        #preorder using stack
        s = [root]
        summ = 0
        while s:
            subroot = s.pop()
            
            #if left node is leaf, add its value
            if isleaf(subroot.left):
                summ += subroot.left.val
            if subroot.right:
                s.append(subroot.right)
            if subroot.left:
                s.append(subroot.left)
                
        return summ
    
    #time o(n) space o(n) concept preorder traversal, stack, dfs