# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        def preorder(root, currSum):
            nonlocal count
            if not root:
                return None
            
            #current prefix sum
            currSum += root.val
            
            #what we are looking for
            if currSum == targetSum:
                count += 1
                
            
            #number of times currsum - targetsum has occured
            #determine the number of times a path with targetsum
            #has occured up to current node
            count += ht[currSum - targetSum]
            
            #add currsum to hashmap during child node processing
            ht[currSum] += 1
            
            
            preorder(root.left, currSum)
            preorder(root.right, currSum)
            
            #remove currsum from hashmap in order to not use it during sibling node processing
            ht[currSum] -= 1
            
        
        count = 0
        ht = defaultdict(int)
        preorder(root, 0)
        return count
    
    #time o(n) space o(n)