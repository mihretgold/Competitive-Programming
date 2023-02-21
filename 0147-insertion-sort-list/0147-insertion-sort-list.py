# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        # initialize dummy next
        dummy.next = head
        curr = head
        insert = head.next
        prev = head
        
        while insert:
            nxt = insert.next
            prevcurr = dummy
            while curr != insert and insert.val > curr.val:
                curr = curr.next
                prevcurr = prevcurr.next
                
            if curr != insert:
                prevcurr.next = insert
                insert.next = curr
                # curr = nxt
                # prev.next points to the inserted node hence prev.next
                prev.next = nxt
            else:
                prev = prev.next
                
            insert = nxt
            curr = dummy.next
            
        return dummy.next
            
                