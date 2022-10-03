class MinStack {
public:
     stack<int> s;
    stack<int> m; 
    MinStack() {
      
    }
    
        void push(int val) {
          
        if(!m.empty() && val >= m.top()){
            m.push(m.top());
        }
        else
            m.push(val);
        s.push(val);
    }

    
    void pop() {
      s.pop();
        m.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return m.top();
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