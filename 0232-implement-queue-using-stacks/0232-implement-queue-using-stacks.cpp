class MyQueue { 
    //To create a queue we use 2 stacks one to push back elements the other to copy elements from the first stack and to remove front elements and peek at the first element
public:
    stack<int>s;
    stack<int>c;
    MyQueue() {
      
    }
    
    void push(int x) {
      s.push(x); 
    }
    
    int pop() {
        int p;
     if(c.empty()){
             while(!s.empty()){
                 c.push(s.top());
                 s.pop();
             }
         }
        p=c.top();
        c.pop();
        return p;
    }
    
    int peek() {
        int p;
        if(c.empty()){
             while(!s.empty()){
                 c.push(s.top());
                 s.pop();
             }
         }
        p=c.top();
        return p;
    }
    
    bool empty() {
        if(s.empty())  return c.empty();
      return false;  
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */