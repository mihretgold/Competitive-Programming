# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        
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
        
        maxi = 0
        while prev and head:
            sum = 0
            if prev != head:
                sum = prev.val + head.val
                maxi = max(maxi, sum)
            else:
                break
            
            head = head.next
            prev = prev.next
            
        return maxi
            
            
        
       