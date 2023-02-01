# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ranges = right - left
        # if not head or not head.next or ranges < 1:
        #     return head
        l = left
        dummy = ListNode(0)
        dummy.next = head
        leftPtr = dummy
        
        while left - 1 > 0 and leftPtr:
            leftPtr = leftPtr.next
            left -= 1
        
        # rightPtr = dummy
        # while right > 0 and rightPtr:
        #     rightPtr = rightPtr.next
        #     right -= 1
        print(leftPtr.val)
        temp = leftPtr.next
        prev = leftPtr.next
        curr = prev.next
      
        while ranges > 0 and curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            ranges -= 1
        print(prev.val)
        leftPtr.next = prev
        temp.next = curr
        if(l == 1): head = prev
        return head
            
        
             
                        
        
        
            