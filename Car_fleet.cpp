class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
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
    }
};
