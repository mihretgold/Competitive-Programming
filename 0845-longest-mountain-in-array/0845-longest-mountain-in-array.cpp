class Solution {
public:
    int longestMountain(vector<int>& arr) {
       int n= arr.size();
        int ans=0;
       for(int i=1; i<=n-2;){
           
           if(arr[i]>arr[i-1]&& arr[i]>arr[i+1]){
               int counts=1;
               int j=i;
               while(j>0 && arr[j]>arr[j-1]){
                   j--;
                   counts++;
               }
               while(i<n-1 && arr[i]>arr[i+1]){
                   i++;
                   counts++;
               }
              ans=max(ans,counts); 
           }
           else{
               i++;
           }
           
       }
        return ans;
    }
};