class Solution {
public:
    /*
    s,e  k=3 count =0 sum=0
    
    22225558   count=3
    ^ ^ 
    
    while e<n
    for(o-k){sum}
    sum/3 >= t -> counts++
    sum-=arr[s];
    s++;
    e++;
    sum+=arr[e];
    
    
    */
     int numOfSubarrays(vector<int>& arr, int k, int threshold) {
      int n= arr.size();
         int l=0,r=0,sum=0,count=0;
         while(r<n){
             while(r-l+1 <= k){
                 sum+=arr[r++];
             }
             if(sum>=k*threshold){
                 count++;
             }
             sum-=arr[l++];
         }
         return count;
    }
};