# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        curr = head
        count = 0
        
        while curr:
            curr = curr.next
            count += 1
        
        if count == 0 or count <= 1 or k < 1 or k % count == 0:
            return head
        
        curr = head
        ranges = (count - (k +1)) % count
        print(ranges)
        while ranges > 0 and curr:
            curr = curr.next
            ranges -= 1
           
        head = curr.next
        curr.next = None
        
        trail = head
        while trail.next:
            trail = trail.next
            
        trail.next = start
        
        return head