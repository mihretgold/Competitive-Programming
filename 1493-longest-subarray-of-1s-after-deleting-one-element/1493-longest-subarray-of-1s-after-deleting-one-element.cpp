class Solution {
public:
    /*int longestSubarray(vector<int>& nums) {
        int n=nums.size(), counts=0,l=0,r=0;
        int m=0;
        while(r<n){
            if(nums[r] == 0)//counts zeros
                counts++;
           while(counts>1){//while there is more than 1 zero increament left pointer
               if(nums[l]==0)
                   counts--;
                   l++;
           }
             r++;
        m=max(m,r-l-1);
           
        }
        return m;
    }*/
    int longestSubarray(vector<int>& nums) {
        int n=nums.size(),count=0,m=0;
        for(int i=0,j=0; i<n; i++){
            if(nums[i]==0){
               count++; 
            }
            while(count>1){
                if(nums[j]==0)count--;
                j++;
            }
            m=max(i-j,m);
        }
        return m;
    }
};