# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #if start l from head, l will stop on the node need to be removed, but we need the previous on to update pointers
        #so start from dummy
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head
        
        #make a gap between l and r by size of n
        while n > 0 and r:
            r = r.next
            n -= 1
        
        #loop until r is at end, l will stop on a node before the one need to be removed
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        
        return dummy.next
        