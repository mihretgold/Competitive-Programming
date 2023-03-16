class MyCircularDeque {
public:
    deque<int>d;
    int m;
    MyCircularDeque(int k) {
       m=k; 
    }
    
    bool insertFront(int value) {
     if(d.size() <m){
       d.push_front(value);
        return true;
     }
        return false;
    }
    
    bool insertLast(int value) {
     if(d.size() <m){
       d.push_back(value);
        return true;
     }
        return false;   
    }
    
    bool deleteFront() {
      if(d.size()){
       d.pop_front();
        return true;
     }
        return false;  
    }
    
    bool deleteLast() {
       if(d.size()){//>0
       d.pop_back();
        return true;
     }
        return false; 
    }
    
    int getFront() {
       if(d.size()){       
        return d.front();
     }
        return -1; 
    }
    
    int getRear() {
       if(d.size()){       
        return d.back();
     }
        return -1;  
    }
    
    bool isEmpty() {
      return (d.size()==0);  
    }
    
    bool isFull() {
      return (d.size()==m);   
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */