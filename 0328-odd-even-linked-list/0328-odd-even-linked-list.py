# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first = head
        temp = first
        ans = temp
        second = head.next
        temp2 = second
        ans2 = temp2
        
        while first and first.next:
            first = first.next.next
            temp.next = first
            if first:
                temp = temp.next
            if second and second.next:
                second = second.next.next
                temp2.next = second
                temp2 = temp2.next
            
            
            
        temp.next = ans2
        
        return ans