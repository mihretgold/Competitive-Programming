class Solution {
public:
    bool isValid(string s) {
        stack <char> c;
        int n = s.length();
        for(int i=0; i<n; i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='['){
             c.push(s[i]); 
            }
            else if(s[i]==')' || s[i]=='}' || s[i]==']'){
            if(c.empty())
                return false;
            else if(s[i] == ')' && c.top() != '(')
                return false;
             else if(s[i] == '}' && c.top() != '{')
                return false;
             else if(s[i] == ']' && c.top() != '[')
                return false;
                else
                    c.pop();
            }  
        }
        if(c.empty())
            return true;
        else
            return false;
    }
};