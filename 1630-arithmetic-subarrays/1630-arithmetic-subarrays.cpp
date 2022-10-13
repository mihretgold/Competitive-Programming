class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
 vector<bool> v;
    for (int i = 0, j = 0; i < l.size(); ++i) {
        vector<int> temp(begin(nums) + l[i], begin(nums) + r[i] + 1);
        sort(begin(temp), end(temp));
        for (j = 2; j < temp.size(); ++j)
            if (temp[j] - temp[j - 1] != temp[1] - temp[0])
                break;
        v.push_back(j == temp.size());
    }
    return v;
    }
};