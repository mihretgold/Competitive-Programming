class Solution {
public:
    static bool cmp(string &a,string &b){
        if(a.size()==b.size()){
            return a<b;
        }
        return a.size() <b.size();
    }
    string kthLargestNumber(vector<string>& nums, int k) {
      sort(nums.begin(),nums.end(),cmp);
        int n=nums.size();
        string ans;
        for(int i=0; i<nums.size(); i++){
            ans=nums[n-k];
            break;
        }
        return ans;
    }
};