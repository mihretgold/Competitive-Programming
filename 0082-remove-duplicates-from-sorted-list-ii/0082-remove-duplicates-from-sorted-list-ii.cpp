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
    /*
     [1,2,3,3,4,4,5]
                ^ ^
     125
    
    */ 
      ListNode* deleteDuplicates(ListNode* head) {
        if(!head || !head->next) return head;
        ListNode *next = head->next;
        
        if(next->val == head->val){
            while(next && next->val == head->val) next=next->next;//skip duplicates
            return deleteDuplicates(next);//delete duplicate elements
        }else{
            head->next = deleteDuplicates(next);
            return head;
        }
    }
};