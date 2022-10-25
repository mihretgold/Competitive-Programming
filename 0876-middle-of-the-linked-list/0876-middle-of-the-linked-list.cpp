/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
       ListNode* slow,* fast;//declare 2 linked list
        fast=slow=head;//start both from head
        while(fast &&fast->next){//while not NULL
            fast=fast->next->next;//goes 2X faster so when it reaches the end the slow will be at the middle
            slow=slow->next;
        }
        return slow;
    }
};