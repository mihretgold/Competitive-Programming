# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        right = head
        
        while right and right.next:
            if right.val == right.next.val:
                right.next = right.next.next
            else:
                right = right.next        
            
            
        return head