# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ht =  defaultdict(int)
        
        def dfs(root):
            if root:
                ht[root.val] += 1
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
                    
        dfs(root)
        most_frequent = max(ht.values())
        
        res = [n for n,f in ht.items() if f == most_frequent]
        
        return res
        
        #time o(n) space o(n) concept tree, hashtable