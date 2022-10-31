class Solution {
public:
    /*
   [1,2,3,4]    
  [24,12,8,6]    
    
    */
    /* BRUTE FORCE TIME LIMIT EXCEED FOR C++
    vector<int> productExceptSelf(vector<int>& nums) {
       int n=nums.size();
        vector<int>ans(n);        
        for(int i=0; i<n; i++){//outer loop to isolate each element and push back to answer vector
          int p=1;//intialize product as 1 not 0 cuz it's not sum
            for(int j=0; j<n; j++){//inner loop to calculate all product exept i index
               if(i==j)continue;
                p*=nums[j];
            }
            ans[i]=p;
        }
        return ans;
    }*/
    vector<int> productExceptSelf(vector<int>& nums) {
       int n=nums.size();
        vector<int>pre(n);
         vector<int>suf(n);
        vector<int>ans(n);
        pre[0]=1;
        suf[n-1]=1;
        
        for(int i=1; i<n; i++){
            pre[i]=pre[i-1]*nums[i-1];
        }
        for(int i=n-2; i>=0; i--){
            suf[i]=suf[i+1]*nums[i+1];
        }
         for(int i=0; i<n; i++){
            ans[i]=pre[i]*suf[i];
        }
        return ans;
    }
};
/* public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int pre[] = new int[n];
        int suff[] = new int[n];
        pre[0] = 1;
        suff[n - 1] = 1;
        
        for(int i = 1; i < n; i++) {
            pre[i] = pre[i - 1] * nums[i - 1];
        }
        for(int i = n - 2; i >= 0; i--) {
            suff[i] = suff[i + 1] * nums[i + 1];
        }
        
        int ans[] = new int[n];
        for(int i = 0; i < n; i++) {
            ans[i] = pre[i] * suff[i];
        }
        return ans;
    }*/