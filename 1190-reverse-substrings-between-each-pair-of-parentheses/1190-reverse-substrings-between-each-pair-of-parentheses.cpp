class Solution {
public:
    string reverseParentheses(string s){
    int n=s.size();
    stack<char>st;
    for(int i=0; i<n; i++){
        //find first 
        if(s[i]==')'){
             string word="";
            while(!st.empty() && st.top() != '('){//to only reverse the elements in the brace
               word+=st.top();
                st.pop();
            }
            st.pop();//to reve the open bracket
            for(char x: word)
              st.push(x);
        }else{
          st.push(s[i]);
        }
    }
        string ans ="";
        while(!st.empty()){//put the reverse elements in the string ans
           ans+=st.top();
            st.pop();
        }
        reverse(ans.begin(), ans.end());//reverse to get orignal answer
    return ans;
}
};
