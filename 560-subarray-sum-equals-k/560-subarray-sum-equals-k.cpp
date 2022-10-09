class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
      int n=nums.size();
        unordered_map<int,int>mp;
        int r=0,counts=0,sum=0;
        while(r<n){
          sum+=nums[r];            
          if(sum ==k){
              counts++; 
             }
          if(mp.find(sum-k)!=mp.end())
              counts+=mp[sum-k];
             mp[sum]++;
            r++;
       } 
        return counts;
    }
};