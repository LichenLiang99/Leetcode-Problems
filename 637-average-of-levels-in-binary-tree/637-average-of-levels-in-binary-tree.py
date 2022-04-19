# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        
        #do bfs with queue
        q = deque([root])
        res = []
        
        while q:
            level = []
            for i in range(len(q)):
                root = q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            
            res.append(sum(level)/len(level))
            
        return res
    #time o(n) space o(n) concept tree, bfs