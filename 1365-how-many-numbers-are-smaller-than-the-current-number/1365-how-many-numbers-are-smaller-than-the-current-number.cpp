class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
       int n=nums.size();
        vector<int>counts(n,0);
                
        for(int i=0; i<nums.size(); i++){
           for(int j=0; j<nums.size(); j++){
             if(nums[i] > nums[j]){
                 counts[i]++;
             }  
           } 
       } 
        return counts;
    }
};