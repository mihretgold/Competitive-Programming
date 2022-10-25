class Solution {
public:
    /*
     [0,1,0,3,12]
     131200
    
    
    */
    void moveZeroes(vector<int>& nums) {
      int n=nums.size();
        vector<int>ans;
        int i,count=0;
        for(i=0;i<n; i++){
            if(nums[i]==0){//when encounter a 0 we increament count
                count++;
            }else{//add non zero elements to ans vector
                ans.push_back(nums[i]);
            }
        }
        for(i=0; i<count; i++){//we push back count number of 0's to the end
            ans.push_back(0);
        }
        for(i=0;i<n; i++){
           nums[i]=ans[i];
        }
        //return ans;
    }
};