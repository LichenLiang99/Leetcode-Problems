"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        maxDepth = 0
        q = deque()
        q.append(root)
        
        while q:
            maxDepth += 1
            level_length = len(q)

            for _ in range(level_length):
                node = q.popleft()
                q += [cld for cld in node.children]
        
        return maxDepth
                