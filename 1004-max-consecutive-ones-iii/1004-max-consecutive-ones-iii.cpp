class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
      int n= nums.size();
      int j=0,  counts=0, z=0;
      int m=0;
     
        for(int i=0; i<n; i++){
            if(nums[i] == 0) z++;
            while(z>k){
                if(nums[j]==0) z--;
                j++;
            }
            m= max(m, i-j+1);
        }
        return m;
    }
};