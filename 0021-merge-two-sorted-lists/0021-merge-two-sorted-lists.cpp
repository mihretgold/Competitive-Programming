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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
       if(!l1) return l2;
       if(!l2) return l1;
        
        ListNode* head=l1;
        if(l2->val < l1->val){
            head=l2;
            l2=l2->next;            
        }
        else{
            l1=l1->next;
        }
        ListNode* curr=head;
        
        while(l1 && l2){
        if(l2->val > l1->val){
            curr->next=l1;
            l1=l1->next;
        }
        else{
            curr->next =l2;
            l2=l2->next;
        }
            curr=curr->next;
        }
        if(!l1) curr->next=l2;
        else curr->next=l1;
        
        return head;
    }
};