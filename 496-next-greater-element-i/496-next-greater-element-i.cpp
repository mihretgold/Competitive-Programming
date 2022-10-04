class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
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
    }
};