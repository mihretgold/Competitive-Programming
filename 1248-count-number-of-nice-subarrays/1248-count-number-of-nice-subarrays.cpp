class Solution {
public:
    int numberOfSubarrays(vector<int>arr, int k){
    int n=arr.size();
    int r=0,l=0;
    int oc=0,count=0,ans=0;
    
    while(r<n){
        if(arr[r] %2!=0){//if the num is odd increament oc and r ptr
            oc++;
            count=0;
        }
        while(oc==k) { //if have the num odd numbers we need in the subarray
            count++;
           if(arr[l]%2!=0) oc--;  //if the left ptr was on an odd number 
            l++;
             
        }
        ans+=count;
            r++;
    }
    
      return ans;
    }
};
