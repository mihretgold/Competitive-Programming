# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        temp = head
        less = dummy
        less_head = less
        great = ListNode(-1)
        great_head = great
        count = 0
        
        while temp:
            if temp.val < x:
                less.next = temp
                less = less.next
            else:
                great.next = temp
                great = great.next
            temp = temp.next
          
        great.next = None
        less.next = great_head.next
        
        return less_head.next
            
   
        
                    
                
                