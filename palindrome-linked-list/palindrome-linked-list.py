# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        #change to array then use 2 pointers to converge
        num = []
        
        while head:
            num.append(head.val)
            head = head.next
        
        l, r = 0, len(num) - 1
        
        while l <= r:
            if num[l] != num[r]:
                return False
            l += 1
            r -= 1
        
        return True

        #find midpoint of list then reverse the second half and check
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse, prev is the starting point of reversed half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #check
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
            
        return True