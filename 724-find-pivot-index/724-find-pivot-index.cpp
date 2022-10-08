class Solution {
public:
    int pivotIndex(vector<int>& nums) {
     int sum=0;
        for(int i: nums){
            sum += i;
        }
        int p=0;
        for(int i=0; i<nums.size(); i++){
            if(sum-p-nums[i] == p){
                return i;
            }
            p+=nums[i];
        }
      return -1; 
    }
};