# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
#         if not root:
#             return 0
#         else:
#             stack, min_depth = [(1, root),], float('inf')
        
#         while stack:
#             depth, root = stack.pop()
#             children = [root.left, root.right]
#             if not any(children):
#                 min_depth = min(depth, min_depth)
#             for c in children:
#                 if c:
#                     stack.append((depth + 1, c))
        
#         return min_depth 

        # bfs
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        minDepth = 0
        
        while q:
            minDepth += 1
            level_length = len(q)

            for _ in range(level_length):
                node = q.popleft()

                if not node.left and not node.right:
                    return minDepth

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)