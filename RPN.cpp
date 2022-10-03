class Solution {
public:
    int evalRPN(vector<string>& tokens) {
     stack <int> s;
    
        for(string x: tokens){
            
            if(x=="+"){
               int p=s.top();
                s.pop();
               int q=s.top();
                s.pop();
                s.push(p+q);
            }
           else if(x=="-"){
               int p=s.top();
                s.pop();
               int q=s.top();
                s.pop();
                s.push(q-p);
            }
           else if(x=="*"){
               int p=s.top();
                s.pop();
               int q=s.top();
                s.pop();
                s.push(p*q);
            }
           else if(x=="/"){
                int p=s.top();
                s.pop();
               int q=s.top();
                s.pop();
               s.push(q/p);
            }         
           else {
              s.push(stoi(x));
            }
        }
      
        return s.top();
    }
};
