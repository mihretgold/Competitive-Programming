class Solution {
public:
   /* SPACE COMPLEXITY O(N)
   vector<int> sortArrayByParityII(vector<int>& nums) {
        vector<int>even;
        vector<int>odd;
        vector<int>ans;
      for(int i=0; i<nums.size(); i++){
         if(nums[i]%2==1){//add odd nums to odd array
           odd.push_back(nums[i]);
         }else{// add even nums to even array
             even.push_back(nums[i]);
         } 
      }
        for(int i=0; i<even.size(); i++){//add even then odd nums to ans array
            ans.push_back(even[i]);
            ans.push_back(odd[i]);
        }
        return ans;
    }*/
    // SPACE COMPLEXITY O(1)
    vector<int> sortArrayByParityII(vector<int>& nums) {
        int i=0,j=1,n=nums.size();
        while(i<n && j<n){
            if(nums[i]%2==0){//if even
                i+=2;
            }else if(nums[j]%2!=0){//if odd
                j+=2;
            }else{//if in wrong order
                swap(nums[j],nums[i]);
                i+=2;
                j+=2;
            }
        }
        
        return nums;
    }
};