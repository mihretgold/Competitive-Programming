class Solution {
public:
   vector<int> findOriginalArray(vector<int>& A) {
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
    }
};

/**/