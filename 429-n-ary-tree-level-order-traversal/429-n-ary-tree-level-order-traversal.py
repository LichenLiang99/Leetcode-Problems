"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if not root:
            return result

        q = deque()
        q.append(root)

        while q:
            level_length = len(q)
            curr_level = []
            for _ in range(level_length):
                node = q.popleft()
                curr_level.append(node.val)
                for cld in node.children:
                    q.append(cld)

            result.append(curr_level)
        return result