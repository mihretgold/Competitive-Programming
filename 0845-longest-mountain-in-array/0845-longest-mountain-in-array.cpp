class Solution {
public:
    /*
    Algorithm
    1) initialize a for loop from 1 to n-2 because the last ans first elements can't be a peak
    2) if the num b/f & a/f the element are < then we have a peak
    3) we start count from 1 for the peak and increament it if the elements to the right and left are proggresively smaller
    4) store it in a max variable
    5) if it's not a peak we simply increament the ptr
    6) return the max variable
    
    
    */
    int longestMountain(vector<int>& arr) {
       int n= arr.size();
        int ans=0;
       for(int i=1; i<=n-2;){//n-2 b/c peak can't be in the last element
           
           if(arr[i]>arr[i-1]&& arr[i]>arr[i+1]){//first we find the peak
               int counts=1;
               int j=i;
               while(j>0 && arr[j]>arr[j-1]){// then we decreament to its left as long as it less
                   j--;
                   counts++;
               }
               while(i<n-1 && arr[i]>arr[i+1]){// then we increament to its right as long as it less
                   i++;
                   counts++;
               }
              ans=max(ans,counts); //return max count
           }
           else{// if peak is not found we increament ptr
               i++;
           }
           
       }
        return ans;
    }
};