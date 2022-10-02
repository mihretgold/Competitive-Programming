class Solution {
public:
    
    int maxOperations(vector<int>& nums, int k) {
      int counts=0,n=nums.size();
      sort(nums.begin(), nums.end());        
        int i=0,j=n-1;
        while(i<j){
            int sum = nums[i]+nums[j];
            if(sum==k){
                i++;
                j--;
                counts++;
            }
            else if(sum<k){
                i++;
            }
            else if(sum>k){
                j--;
            }
            
        }
     return counts;
    }
};