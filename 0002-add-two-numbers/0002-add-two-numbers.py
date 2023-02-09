# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        
        curr1 = l1
        while curr1:
            str1 += str(curr1.val)
            curr1 = curr1.next
            
        curr2 = l2
        while curr2:
            str2 += str(curr2.val)
            curr2 = curr2.next
        str1 = str1[::-1]  
        str2 = str2[::-1]
        num1 = int(str1)
        num2 = int(str2)
        ans = str(num1 + num2)
        
        
        head = ListNode(ans[0])
        length = len(ans)
        index = 1
        while index < length:
            curr = ListNode(ans[index])
            temp = head
            curr.next = temp
            head = curr
            index += 1
            
        return head