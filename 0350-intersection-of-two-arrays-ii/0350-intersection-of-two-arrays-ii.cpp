class Solution {
public:
   /*nums1 = [4,9,5], nums2 = [9,4,9,8,4]
     4 5 9    ans={4,}  if nums2 < nums1 j++
         i
     
     4 4 8 9 9
           j
    
    
    */
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
     int n= nums1.size(), l=nums2.size();
        int i=0,j=0,a=0;
        vector<int>ans;
        sort(nums1.begin(),nums1.end());
         sort(nums2.begin(),nums2.end());
        while(i<n && j < l){
            if(nums1[i]==nums2[j]){//find similar elements
                int a=nums1[i];
              ans.push_back(a);
                i++; j++;
            }else if(nums2[j] < nums1[i]){// if not similar and nums2 is less
                j++;
            }else{//if not similar and nums1 is less
                i++;
            }
        }
        return ans;
    }
};