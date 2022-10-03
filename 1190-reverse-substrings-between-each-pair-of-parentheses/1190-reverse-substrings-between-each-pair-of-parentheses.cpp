class Solution {
public:
    string reverseParentheses(string s) {
    stack<char> a;
   
    int n = s.size();
        for(int i=0; i<n; i++){
          if(s[i]!=')')
            a.push(s[i]);
        else{
             string word="";
        while(!a.empty()&&a.top()!='('){
              word+=a.top();
              a.pop();
            } 
            a.pop();
            for(int i=0; i<word.size(); i++)
                a.push(word[i]);
          }
        }
        string ans="";
        while(!a.empty()){
            ans+= a.top();
            a.pop();
        }
        reverse(ans.begin(), ans.end());
      return ans;  
    }
};
