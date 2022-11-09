class Solution {
public:
    
    int maxOperations(vector<int>& nums, int k) {
     sort(nums.begin(),nums.end());
        int s=0, e=nums.size()-1,count=0;
        while(s<e){
            if(nums[s]+nums[e]==k){
                count++;
                s++; e--;
            }else if(nums[s]+nums[e] >k){//because the greater numbers are at the end
                 e--;
            }else if(nums[s]+nums[e] <k){//because the smaller numbers are the start
                 s++;
            }
        }
        return count;
    }
};