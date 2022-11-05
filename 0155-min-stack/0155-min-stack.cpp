class MinStack {
public: 
    /*
    make 2 stakes one to store values and the other to store the min values make both on push function
    */
    stack<int>s;
    stack<int>c;
    MinStack() {
      
    }
    
    void push(int val) {
       if(!c.empty() && val>=c.top()){//if min stack is not empty and the new element < push the last element
           c.push(c.top());
       }else{//if min stack is empty of the new element > push the new element
           c.push(val);
       }
         s.push(val);//store all values
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