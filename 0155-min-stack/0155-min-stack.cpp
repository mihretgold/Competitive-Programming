class MinStack {
public: 
    stack<int>s;
    stack<int>c;
    MinStack() {
      
    }
    
    void push(int val) {
       if(!c.empty() && val>=c.top()){
           c.push(c.top());
       }else{
           c.push(val);
       }
         s.push(val);
    }
    
    void pop() {
       s.pop();
        c.pop();
    }
    
    int top() {
      return s.top(); 
    }
    
    int getMin() {
      return c.top();  
    }
};


/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */