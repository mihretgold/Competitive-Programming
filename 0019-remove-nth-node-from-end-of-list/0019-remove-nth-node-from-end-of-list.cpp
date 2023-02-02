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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *temp=new ListNode(0);
        temp->next = head;
        ListNode *slow=temp;
        ListNode *fast=temp;
        
        int x=0;
        while(x<n+1 && fast)
        {
            fast=fast->next;
            x++;
        } 
        while(fast != NULL)
        {
            fast=fast->next;
            slow=slow->next;
        }
        cout<<slow->val<<endl;
        if (slow && slow->next)
        {
            slow->next = slow->next->next;
        }
        
        return temp->next;
        
    }
};
