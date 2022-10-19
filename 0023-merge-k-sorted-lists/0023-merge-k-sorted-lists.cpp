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
    /*
    compare elements then add the smallest
    
    */
public:
    class Cmp{
        public: 
         bool operator()(ListNode *a, ListNode *b){
        return a->val > b->val;
    }
    };
    ListNode* mergeKLists(vector<ListNode*>& lists) {
      
        priority_queue<ListNode* , vector<ListNode*>, Cmp>pq;
        for(auto x: lists)
            if(x) pq.push(x);
        if(pq.empty()) return NULL;
        ListNode *head=pq.top();
        pq.pop();
        if(head->next) pq.push(head->next);
        head->next =NULL;
        ListNode *curr = head;
        while(!pq.empty()){
            ListNode *n =pq.top();
            pq.pop();
            curr->next =n;
            curr =n;
            if(n->next) pq.push(n->next);
            
        }
        return head;
    }
};