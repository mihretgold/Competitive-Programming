class Solution {
public:
   
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector<int>ans(1001);// since trip length is 1<= l <=1000
        for(auto x: trips){ // add passengers at the begining of trip and reduce at each end of trip
         ans[x[1]]+=x[0];
         ans[x[2]]-=x[0];
        }
        for(auto x: ans){ // subtracting capacity from number of passengers at each pt if <0 it exceeds capacity
           capacity-=x;
            if(capacity <0){
                return false;
            }
        }
        return true;
    }
};