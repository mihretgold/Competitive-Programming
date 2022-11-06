class Solution {
public:
    /*BRUTE FORCE APROCH
    TIME COMPLEXITY=O(N*M) SPACE COMPLEXITY= O(N)
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
        for(int i=0; i<n; i++){//checkes if the next element is greater
            for(int j=foundIdx[i] + 1; j<l; j++){//put the index of next element on j
               if(nums2[j]>nums2[foundIdx[i]]){
                   ans[i]=nums2[j];
                   break;
               }
           }
            if(ans[i]==0) ans[i]=-1;
        }
        return ans;
    }*/
     vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size(),l=nums2.size();
        stack<int>s;
         s.push(-1);
         unordered_map<int,int>mp;
         for(int i=l-1; i>=0; i--){//store next greater element on map
            while(s.top()!=-1 && nums2[i] > s.top()) s.pop();
             mp[nums2[i]]=s.top();
             s.push(nums2[i]);
         }
         for(int i=0; i<n; i++){//store next greater of nums1 
             nums1[i]=mp[nums1[i]];
         }
         return nums1;
    }
};
