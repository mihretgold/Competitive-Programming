class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int>p(nums.begin(),nums.end());
        vector<int>v;
        while(!p.empty()){
            v.push_back(p.top());
            p.pop();
        }
        int ans=v[k-1];
        return ans;
    }
};