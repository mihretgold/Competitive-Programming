class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> counts;
        for(auto i : words){
            counts[i]++;
        }
        
        auto comp = [&](const pair<string,int>& a, const pair<string,int>& b) {
            return a.second > b.second || (a.second == b.second && a.first < b.first);
        };
        typedef priority_queue< pair<string,int>, vector<pair<string,int>>, decltype(comp) > my_priority_queue_t;
        my_priority_queue_t  p(comp);
        
        for(auto i : counts ){
            p.emplace(i.first, i.second);
            if(p.size()>k) p.pop();
        }
        
        vector<string> v;
        while(k--){
            v.insert(v.begin(), p.top().first);
            p.pop();
        }
        return v;
    }
};