# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            duplicate = True
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                duplicate = False
            if duplicate:
                prev.next = curr
                prev = prev.next
            
            if curr:
                curr= curr.next
        prev.next = curr
        return dummy.next