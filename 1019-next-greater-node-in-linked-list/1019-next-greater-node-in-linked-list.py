# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        stack = []
        ans = []
        while prev:
            if len(stack) == 0:
                ans.append(0)
                stack.append(prev.val)
                prev = prev.next
            elif stack[-1] > prev.val:
                ans.append(stack[-1])
                stack.append(prev.val)
                prev = prev.next
            elif stack[-1] <= prev.val:
                stack.pop()
        ans.reverse()
        
                
        return ans
            
                
           