class Solution {
public:
   /* vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> v(nums2.size(),-1); 
        stack<int> s;
        vector<int> r(nums1.size());
        for(int i=0; i<nums2.size(); i++){
          int a=nums2[i];
            while(!s.empty() && nums2[s.top()]<a){
                v[s.top()]=a;
                s.pop();
            }
            s.push(i);
        }
        for(int i=0; i<nums1.size(); i++){
            int p=find(nums2.begin(), nums2.end(), nums1[i]) - nums2.begin();
            r[i]=v[p];
        }
        return r;
    }*/
    //BRUTE FORCE APROCH
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size(),l=nums2.size();
        vector<int>foundIdx(n);
        for(int i=0; i<n; i++){//store the indexes that nums1 is found on nums2
            for(int j=0; j<l; j++){
               if(nums1[i]==nums2[j]) foundIdx[i]=j;
           }
        }
        vector<int>ans(n);
        int idx=0;
        for(int i=0; i<n; i++){
            for(int j=foundIdx[i] + 1; j<l; j++){
               if(nums2[j]>nums2[foundIdx[i]]){
                   ans[i]=nums2[j];
                   break;
               }
           }
            if(ans[i]==0) ans[i]=-1;
        }
        return ans;
    }
    
};
