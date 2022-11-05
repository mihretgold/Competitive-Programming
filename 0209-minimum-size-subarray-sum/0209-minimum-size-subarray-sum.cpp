class Solution {
public:
    /*
    sum =0
    21243
      ^ ^
    n,r,l ,m
    while(l<n)
    sum+nums
    l++
    while sum >=
    sum-=nums[r]
    r++
    
    */
    int minSubArrayLen(int target, vector<int>& nums) {
        int n=nums.size();
        int r=0, l=0,mini=n+1, sum=0;
        while(r<n){
              sum+=nums[r++];        
          while(sum >= target){
              mini=min(mini,r-l);//we make mini inside while loop to make sure subarray sum > target
              sum-=nums[l++];               
          }          
            
        }
        return mini==n+1?0:mini;
    }
};
 