class StockSpanner {
public:
     stack<pair<int,int>> s;
    StockSpanner() {
        
    }
    
    int next(int price) {
        int count=0;
        while(!s.empty() && s.top().first<=price){//if the stack holds smaller values
            count+=s.top().second;//add its counts to count
            s.pop();
        }
        count++;//add it's own count
        s.push({price,count});
        return count;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */