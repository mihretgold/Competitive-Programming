class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
      unordered_map<int,int>mp;
       int n=nums.size(); 
        for(int i=0;i<n; i++){
            if(nums[i]&1)
                nums[i]=1;
            else
                nums[i]=0;
        }
        int sum=0,i,counts=0;
        for(i=0;i<n;i++){
            sum+=nums[i];
            if(sum==k)
                counts++;
            if(mp.find(sum-k)!=mp.end())
                counts+=mp[sum-k];
            mp[sum]++;
        }
        return counts;
    }
};