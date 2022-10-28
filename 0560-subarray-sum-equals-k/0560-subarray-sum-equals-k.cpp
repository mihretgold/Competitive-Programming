class Solution {
public:
    /*
    [1,1,1], k = 2 
    
    */
    int subarraySum(vector<int>& nums, int k) {
      int n=nums.size();
        unordered_map<int,int>mp;
        int r=0,counts=0,sum=0;
        while(r<n){
          sum+=nums[r++];// add elements to the sum        
          if(sum ==k){// if sum=k increament sum
              counts++; 
             }
          if(mp.find(sum-k)!=mp.end())//if we find sum-k that means there are subarrays of the counts of sum -k for eg if sum = 15 and their is (1) 5=sum-k sum stored there can be a subararay after that too 15 w/c is 10
              counts+=mp[sum-k];
             mp[sum]++;//store the sums and thier counts
       } 
        return counts;
    }
};
