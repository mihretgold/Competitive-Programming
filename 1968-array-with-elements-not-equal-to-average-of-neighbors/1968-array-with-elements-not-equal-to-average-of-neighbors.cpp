class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int temp;
     for(int i=1; i<nums.size()-1; i++){
         if((nums[i-1] > nums[i] && nums[i]> nums[i+1]) ||(nums[i-1] < nums[i] && nums[i]< nums[i+1])){
             temp = nums[i];
             nums[i]=nums[i+1];
             nums[i+1]=temp;
         }
     } 
        return nums;
    }
};