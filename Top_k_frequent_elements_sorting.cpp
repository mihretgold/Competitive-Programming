class Solution {
public:
    static bool cmp(pair<int,int>&a ,pair<int,int>&b){
return a.second>b.second;
}
    vector<int> topKFrequent(vector<int>& nums, int k) {
       unordered_map<int,int>counts;
      // priority_queue<pair<int,int>, vector<pair<int,int>>,greater<pair<int,int>>>p;
        
        for(auto i: nums){
            counts[i]++;
        }
        vector<pair<int,int>> v(counts.begin(),counts.end());
    
        sort(v.begin(),v.end(),cmp);
        
        vector<int>result;
        for(int i=0; i<k; i++){
            result.push_back(v[i].first);
                  
        }
        return result;
    }
};
