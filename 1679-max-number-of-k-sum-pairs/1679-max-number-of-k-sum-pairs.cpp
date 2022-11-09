class Solution {
public:
    
    int maxOperations(vector<int>& nums, int k) {
     sort(nums.begin(),nums.end());
        int s=0, e=nums.size()-1,count=0;
        while(s<e){
            if(nums[s]+nums[e]==k){
                count++;
                s++; e--;
            }else if(nums[s]+nums[e] >k){
                 e--;
            }else if(nums[s]+nums[e] <k){
                 s++;
            }
        }
        return count;
    }
};