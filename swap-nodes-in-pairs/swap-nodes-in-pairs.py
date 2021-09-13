# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        p1 = head
        
        while p1 and p1.next:
            #save pointers
            nextpair = p1.next.next
            p2 = p1.next
            
            #reverse
            p2.next = p1
            p1.next = nextpair
            prev.next = p2
            
            #update
            prev = p1
            p1 = nextpair
            
        return dummy.next
    
    #time o(n) space o(1) concept linked list