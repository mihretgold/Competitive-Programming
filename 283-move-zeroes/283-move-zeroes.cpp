class Solution {
public:
    void moveZeroes(vector<int>& nums) {
     int r=0, l=0,temp, n= nums.size();
        if(n==0||n==1)
            return;
        while(r<n){
            if(nums[r]==0){
                r++;
            }
            else{
               temp = nums[l];
                nums[l]= nums[r];
                nums[r]=temp;
                r++;
                l++;
            }
        }
    }
};