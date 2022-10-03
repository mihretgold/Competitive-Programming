class Solution {
public:
  string reverseParentheses(string s) {
        stack<char>stk;
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]!=')')
                stk.push(s[i]);
            else
            {
                string ss="";
                while(!stk.empty()&&stk.top()!='(')
                {
                    ss+=stk.top();
                    stk.pop();
                }
                stk.pop();
                for(int i=0; i<ss.size(); i++)
                    stk.push(ss[i]);
            }
        }
        string ans="";
        while(!stk.empty())
        {
            ans+=stk.top();
            stk.pop();
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
