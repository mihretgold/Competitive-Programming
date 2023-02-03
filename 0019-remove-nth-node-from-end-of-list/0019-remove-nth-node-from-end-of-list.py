# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        # dummy = ListNode(-1)
        # dummy.next = head
        curr = head
        while curr:
            curr = curr.next
            index += 1
        
        ranges = index - (n + 1)
        if ranges  == -1:
            head = head.next
            return head
        print(ranges)
        
        # node = head
        # while node:
        #     print(node.val)
        #     node = node.next
        # print(index)
        
        curr = head
        while ranges > 0:
            curr = curr.next
            ranges -= 1
            
        if not head or not head.next:
            head = None
        elif curr and curr.next:
            curr.next = curr.next.next
            
        return head
            
        