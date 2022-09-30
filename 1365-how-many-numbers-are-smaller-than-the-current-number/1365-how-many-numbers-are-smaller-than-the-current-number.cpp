class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
       vector<int>counts;
        
        for(int i=0; i<nums.size(); i++){
           counts.push_back(0);
       } 
        
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