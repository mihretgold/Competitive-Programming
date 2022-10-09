class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n=nums.size(), counts=0,l=0,r=0;
        int m=0;
        vector<int>::iterator i;
        while(r<n){
            if(nums[r] == 0)
                counts++;
           while(counts>1){
               if(nums[l]==0)
                   counts--;
                   l++;
           }
             r++;
        m=max(m,r-l-1);
           
        }
        return m;
    }
};