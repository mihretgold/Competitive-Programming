class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        vector<int> find;
        int l=nums.size();
        int temp;
        /*for(int i=0; i<l - 1; i++){
            for(int j=0; j<l-i-1; j++){
          if(nums[j] > nums[j+1]){
             temp =nums[j];
             nums[j] =nums[j+1];
             nums[j+1] = temp;
          }
        }
        }*/
        sort(nums.begin(),nums.end());
        for(int i=0; i<nums.size(); i++){
            if(target !=0 && nums[i]==target){
                find.push_back(i);
            }
        }
        return find;
    }
};