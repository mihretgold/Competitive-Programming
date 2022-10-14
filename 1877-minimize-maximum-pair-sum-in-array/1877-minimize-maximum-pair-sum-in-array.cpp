class Solution {
public:
    int minPairSum(vector<int>& nums) {
     const int n=nums.size();
      int m=0;
      sort(nums.begin(),nums.end());  
      for(int i=0; i<n/2; i++){
          m=max(m,nums[i]+nums[n-i-1]);
      }
      
     return  m;  
    }
};