# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            curr= head.next        
            prev = head
            prev.next = None
            nxt = curr.next
            while nxt != None:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = nxt.next
            
            curr.next = prev
            return curr
        else:
            return head