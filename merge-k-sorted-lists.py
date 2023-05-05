# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = ListNode(-1)
        temp = answer
        heap = []
        length = len(lists)
        for i in range(length):
            if lists[i]:
                heappush(heap, (lists[i].val, i))

        while heap:
            val, index = heappop(heap)
            answer.next = ListNode(val)
            answer = answer.next
            if lists[index]:
                lists[index] = lists[index].next
                if lists[index]:
                    heappush(heap, (lists[index].val, index))

            
            
        return temp.next