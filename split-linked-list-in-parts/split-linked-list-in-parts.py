# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        #find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        partlength = length // k
        leftover = length % k
        
        res = []
        prev = ListNode(0)
        curr = head
        for i in range(k):
            if i < leftover:
                remainder = 1
            else: 
                remainder = 0
                
            res.append(curr)
            for j in range(partlength + remainder):
                prev = curr
                curr = curr.next
                
            prev.next = None
        
        return res
    
    #time o(n+k), space o(k), concept linked list