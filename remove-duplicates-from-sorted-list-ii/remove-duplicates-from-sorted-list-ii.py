# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        p2 = head
        while p2:
            if p2.next and p2.val == p2.next.val:
                while p2.next and p2.val == p2.next.val:
                    p2 = p2.next
                prev.next = p2.next
            else:
                prev = prev.next
            
            p2 = p2.next
        
        return dummy.next
    
    #time o(n), space o(1), concept, linked list, 2 pointer
                