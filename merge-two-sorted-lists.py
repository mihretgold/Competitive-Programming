# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        
        def merge(list1, list2, answer):
            if not list1 and not list2:
                answer.next = None
                return answer 
            if list1 and not list2:
                answer.next = list1
                return answer
            if list2 and not list1:
                answer.next = list2
                return answer

            if list1.val < list2.val:
                answer.next = list1
                merge(list1.next, list2, answer.next)
            else:
                answer.next = list2
                merge(list1, list2.next,answer.next)    
            
            return answer

        answer = merge(list1, list2, answer)
        return answer.next