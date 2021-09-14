# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #Recursive method---------------
        # s = []
        # root
        # self.helper(root, s)
        # return s[k-1]

#     def helper(self, root, s):

#         if root:
#             self.helper(root.left, s)
#             s.append(root.val)
#             self.helper(root.right, s)
    #end recursive---------------------
    #iterative method---------------
        s = []
        n = 0
        curr = root
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
                
            curr = s.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
    #end iterative---------------------
        
        #time o(n) space o(n) concept inorder traversal, tree




   