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
    1221
    21
    Algorithm                              
    1) copy store the element        OR 1)check if the begining and ending are equal
    2) then reverse the element         2) with 2ptrs until equal
    3) compare                          
     
    
    */
    bool isPalindrome(ListNode* head) {
      vector<int>ans;
        while(head){//while not NULL
            ans.push_back(head->val);//copy list to vector
            head=head->next;//increament list
        }
        int s=0,e=ans.size()-1;
        while(s<e){
            if(ans[s]!=ans[e])//compare numbers
                return false;
                s++;
                e--;
        }
        return true;
    }
};