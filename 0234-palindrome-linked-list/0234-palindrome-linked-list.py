# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = True
        slow = head
        fast = head
        trail = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        curr = slow
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        
        while prev and head:
            if head.val != prev.val:
                check = False
                break
                
            prev = prev.next
            head = head.next
            
        return check