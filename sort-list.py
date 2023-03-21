# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1)
        dummy = temp
        
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2 
                list2 = list2.next
            dummy = dummy.next
                
        if list1:                 
            dummy.next = list1
            
        if list2:
            dummy.next = list2
            
       
        return temp.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None  
        left = self.sortList(head)
        right = self.sortList(temp)
        
        return self.mergeTwoLists(left, right)