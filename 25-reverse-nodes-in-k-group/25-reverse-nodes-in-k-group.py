# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head
        dummy = next_head = ListNode(0, head)
        curr = prev = head

        while True:
            count = 0
            while curr and count < k:
                count += 1
                curr = curr.next

            if count == k:
                h = curr
                t = prev
                for i in range(k):
                    temp = t.next
                    t.next = h
                    h = t
                    t = temp

                next_head.next = h
                next_head = prev
                prev = curr
            else:
                return dummy.next