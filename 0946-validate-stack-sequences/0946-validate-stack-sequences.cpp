class Solution {
public:
    /*
pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
s={1,2}
pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
i=0,j=0
push into s i++ until s.top()==j
s.pop() j++

*/
    bool validateStackSequences(vector<int> &pu,vector<int> &po){
    int n=po.size(), l=pu.size();
    int i=0,j=0;
    stack<int>s;
    while(i < l){
         s.push(pu[i++]);//push elements to stack
        while(!s.empty() && s.top()==po[j]){//while top element of stack is equal to popped element we pop the elements
           s.pop();
            j++;
        }
    }
    return s.empty();
}
};