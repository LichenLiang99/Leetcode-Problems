# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        #do bfs and add right element first
        #the last added value is at bottom left
        queue = [root]
        for root in queue:
            if root.right:
                queue += [root.right]
            if root.left:
                queue += [root.left]
                
        return root.val
    #time o(n) space o(n) concept tree, queue, bfs
    
    
#         q = deque()
#         q.append(root)
#         while q:
#             root = q.popleft()
#             if root.right:
#                 q.append(root.right)
#             if root.left:
#                 q.append(root.left)
                
#         return root.val