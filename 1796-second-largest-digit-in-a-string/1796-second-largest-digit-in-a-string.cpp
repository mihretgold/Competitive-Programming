class Solution {
public:
    int secondHighest(string s) {
       int n=s.size(),k=2;
        unordered_map<int,int>m;
        priority_queue<int,vector<int>,greater<int>>pq;
        for(int i=0; i<n; i++){
            if(s[i]>= 48 && s[i]<=57){
                m[s[i]-48]++;
            }
        }
        for(auto c: m){
            int i=c.first;
            if(pq.size()< k){
                pq.push(i);
            }else{
                if(i>pq.top()){
                    pq.pop();
                    pq.push(i);
                }
            }
        }
        if(pq.size()!= k) return -1;
        return pq.top();
    }
};