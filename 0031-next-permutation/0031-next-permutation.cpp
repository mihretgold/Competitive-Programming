class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n=nums.size()-1;
        int ipt=0;
        for(int i=n; i>0; i--){
            if(nums[i]>nums[i-1]){
               ipt=i;
                break;
            }
        }
        if(ipt==0){
            sort(nums.begin(),nums.end());
        }
        else{
            int toswap =nums[ipt -1];
            int min=INT_MAX;
            for(int j=ipt; j<=n; j++){
                if(nums[j]-toswap>0 && nums[j]-toswap<min){
                swap(nums[j],nums[ipt-1]);    
                }
            }
            sort(nums.begin()+ipt,nums.end());
        }
    }
};