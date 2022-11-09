class Solution {
public:
   /* int carFleet(int target, vector<int>& position, vector<int>& speed) {
     priority_queue<vector<double>>p;
        for(int i=0; i<position.size(); i++){
          double time=(double)(target - position[i])/speed[i];
            p.push({(double)position[i],(double)speed[i],time});
        }
        if(p.size()==0)return 0;
        int fleet=0;
        while(true){
            if(p.size()==1){
                fleet ++;
                break;
            }
            auto ahead= p.top(); p.pop();
            auto behind = p.top(); p.pop();
            if(ahead[2] >= behind[2]){
                p.push(ahead);
            }
            else{
                fleet++;
                p.push(behind);
            }
        }
        return fleet;
    }*/
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int,int>>nums;
        int n=position.size();
        stack<double>s;
        for(int i=0; i<n; i++){//put the position and speed together so it stays together in sorting
            nums.push_back({position[i],speed[i]});
        }
        sort(nums.begin(),nums.end());
        for(int i=n-1; i>=0; i--){//calculate time and push the next greater elements
            double t= (target-nums[i].first)/((double) nums[i].second);
            if(s.empty()|| s.top()<t){
                s.push(t);
            }
        }
        return s.size();
    }
};