# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            nex = curr.next
            
            if curr.val == val:
                prev.next = nex
            else:
                prev = curr
            
            curr = curr.next
        
        return dummy.next
            