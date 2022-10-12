class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int,vector<int>> p;
        int n=stones.size();
        
        for(int i=0; i<n; i++){
            p.push(stones[i]);
        }
        while(p.size()>1){
          int temp=p.top();
          p.pop();
            if(temp != p.top()){
                int ans=temp-p.top();
                p.pop();
                if(ans!=0){
                p.push(ans);
                }
            }
            else{
                p.pop();
            }
        }
       return p.empty() ? 0 :p.top(); 
    }
};