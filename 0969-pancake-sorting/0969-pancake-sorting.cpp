class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
       vector<int> ans;
        int j,i;
        for (i = arr.size(); i > 0; --i) {
            for (j = 0; arr[j] != i; ++j);
            reverse(arr.begin(), arr.begin() + j + 1);
            ans.push_back(j + 1);
            reverse(arr.begin(), arr.begin() + i);
            ans.push_back(i);
        }
        return ans;  
    }
};