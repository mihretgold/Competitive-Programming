class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       unordered_map<int,int>counts;
       priority_queue<pair<int,int>, vector<pair<int,int>>,greater<pair<int,int>>>p;
        for(auto i: nums){
            counts[i]++;
        }
        for(auto & i:counts){
          p.push({i.second,i.first});
            if(p.size()>k){
                p.pop();
            }
        }
        vector<int>result;
        while(k--){
            result.push_back(p.top().second);
            p.pop();          
        }
        return result;
    }
};