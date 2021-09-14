# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        #recursion
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        #bfs iterative queue
        if not root:
            return 0
        level = 0
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return level
                
        #dfs iterative stack
        if not root:
            return 0
        
        s = [[root, 1]]
        level = 1
        
        while s:
            node, depth = s.pop()
            
            if node:
                level = max(level, depth)
                s.append([node.left, depth + 1])
                s.append([node.right, depth + 1])
        return level
