class Solution {
public:
   bool isValid(string s){
    stack<char>c;
    int n=s.length();
    for(int i=0; i<n; i++){
        if(s[i] =='[' || s[i] =='(' || s[i] =='{'){//if the braces are starting braces we push it to the stack
            c.push(s[i]);
        }else if(s[i] ==']' || s[i] ==')' || s[i] =='}'){// if they are ending braces 
            if(c.empty()) return false;//if stack is empty we return false
            //if it's not the respective brace we return false
            else if(c.top()=='[' && s[i]!=']') return false;
            else if(c.top()=='(' && s[i]!=')') return false;
            else if(c.top()=='{' && s[i]!='}') return false;
            else c.pop();//if it's the right brace we pop it
        }        
    }
    //at the end if all element match they will be popped 
    if(c.empty()) return true;
    else return false;
} 
};