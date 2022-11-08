class Solution {
public:
    string removeKdigits(string num, int k) {
      int n=num.size();
        stack<char>s;
        for(char c:num){//deletes the next greater elements
          while(!s.empty() && k>0 && s.top()>c){
              s.pop(); k--;
          }
            if(!s.empty() || c!='0')//heleps to delete zeros at the front like 0200
                s.push(c);
        }
       while(!s.empty() && k--)//if the number of next greater elements < k we pop elements from the stack until k=0
            s.pop();
        if(s.empty())
            return "0";
       
        num="";
       while(!s.empty()){
           num+=s.top();
           s.pop();
       } 
        reverse(num.begin(), num.end());
        return num;
    }
};