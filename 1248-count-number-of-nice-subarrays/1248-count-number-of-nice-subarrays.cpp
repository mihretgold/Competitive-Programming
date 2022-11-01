class Solution {
public:
    /*TWO POINTER SLIDING WINDOWS METHOD
    int numberOfSubarrays(vector<int>arr, int k){
    int n=arr.size();
    int r=0,l=0;
    int oc=0,count=0,ans=0;
    
    while(r<n){
        if(arr[r] %2!=0){//if the num is odd increament oc and r ptr
            oc++;
            count=0;//to restart count
        }
        while(oc==k) { //if have the num odd numbers we need in the subarray
            count++;
           if(arr[l]%2!=0) oc--;  //if the left ptr was on an odd number 
            l++;
             
        }
        ans+=count;//to store count
            r++;
    }
    
      return ans;
    }*/
    int numberOfSubarrays(vector<int>& nums, int k) {
      unordered_map<int,int>mp;
       int n=nums.size(); 
        for(int i=0;i<n; i++){
            if(nums[i]&1)//change odd numbers to 1
                nums[i]=1;
            else//change even numbers to 0
                nums[i]=0;
        }
        int sum=0,i,counts=0;
        mp[0]=1;//to inrease count when sum ==k
        for(i=0;i<n;i++){
            sum+=nums[i];
           /* if(sum==k)//alternative of mp[0]=1
                counts++;*/
            if(mp.find(sum-k)!=mp.end())//if sum -k is found there is a subarray
                counts+=mp[sum-k];
            mp[sum]++;//store sum in map
        }
        return counts;
    }
    
};
