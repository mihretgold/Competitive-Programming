class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); ++i) {
            int b = nums[i], a = target - b;
            if (mp.count(a)) return {mp[a], i}; // Found pair of (a, b), so that a + b = target
            mp[b] = i;//store the index each element is found in
        }
        return {};
    }
};