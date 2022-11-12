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
        for(i=0;i<n; i++){//put all the elements on ans vector to nums
           nums[i]=ans[i];
        }
        //return ans;
    }
      /* void moveZeroes(vector<int>& nums) {
        int n=nums.size(),r=0,l=0;
           if(n==0||n==1) return;
           while(r<n){
               if(nums[r]==0){//if 0 move r ptr
                   r++;
               }else{//if not swap with the element at the l index and increament both r&l ptr
                   swap(nums[l++], nums[r++]);
               }
           }
    }*/
};