# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr.next:
            curr = curr.next
            index += 1
        print(index)
        
        ranges = index - n
        curr = dummy
        while ranges > 0:
            curr = curr.next
            ranges -= 1 
            
        if curr and curr.next:
            curr.next = curr.next.next
            
        return dummy.next
            
        