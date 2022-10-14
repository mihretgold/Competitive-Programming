class Solution {
public:
    int maxFrequency(vector<int>& nums, long k) {
     sort(nums.begin(), nums.end());  
        int n =nums.size();
        int i=0;
        int ans=0;
        
        for(int j=0; j<n; j++){
            k +=nums[j];
            
            while(k<(long) nums[j]*(j-i+1)){
                k-=nums[i];
                i++;
            }
            ans=max(ans,j-i+1);
        }
        return ans;
    }
};