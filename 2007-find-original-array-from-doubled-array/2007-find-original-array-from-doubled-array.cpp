class Solution {
public:
   /*vector<int> findOriginalArray(vector<int>& A) {
        if (A.size() % 2) return {};
        unordered_map<int, int> m;
        for (int a : A) m[a]++;
        vector<int> keys;
        for (auto it : m)
            keys.push_back(it.first);
        sort(keys.begin(), keys.end(), [](int i, int j) {return abs(i) < abs(j);});
        vector<int> res;
        for (int x : keys) {
            if (m[x] > m[2 * x]) return {};
            for (int i = 0; i < m[x]; ++i, m[2 * x]--)
                res.push_back(x);
        }
        return res;
    }*/
    vector<int> findOriginalArray(vector<int>& changed) {
    unordered_map<int, int> m;
    vector<int> v;
    
    sort(changed.begin(), changed.end());
    for(int x: changed){
        if(m[x] == 0) {//add unique smallest elements to the map
            v.push_back(x);
            m[2*x]++;//add the double element so it wont be considered as unique when the loop reaches it
        }
        else {
            m[x]--;
        }       
    }
    return (v.size() == changed.size()/2) ? v : vector<int>{} ;
    }
};

/**/