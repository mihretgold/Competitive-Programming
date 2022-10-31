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
   /*USING PARTIAL SUM
   vector<int> productExceptSelf(vector<int>& nums) {
       int n=nums.size();
        vector<int>pre(n);
         vector<int>suf(n);
        vector<int>ans(n);
        pre[0]=1;//start with idx 0 as 1 so the first element can be excluded and the ans coud be the suffix * 1
        suf[n-1]=1;
        
        for(int i=1; i<n; i++){//array of prefix
            pre[i]=pre[i-1]*nums[i-1];
        }
        for(int i=n-2; i>=0; i--){//array of suffix
            suf[i]=suf[i+1]*nums[i+1];
        }
         for(int i=0; i<n; i++){//ans vectors
            ans[i]=pre[i]*suf[i];
        }
        return ans;
    }*/
    //DECREASED SPACE COMPLEXITY
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int> answer(n, 1);
        for (int i = 1; i < n; i++) {//prefix product
            answer[i] = nums[i - 1] * answer[i - 1];
        }
        int prevProduct = 1;
        for (int i = n - 2; i >= 0; i--) {
            int product = nums[i + 1] * prevProduct;//suffix product
            answer[i] = answer[i] * product;//ans vector (prefix * suffix)
            prevProduct = product;//storing sufix product of previous deacresing space complexity ot suffix array
        }
        return answer;
    }
};
