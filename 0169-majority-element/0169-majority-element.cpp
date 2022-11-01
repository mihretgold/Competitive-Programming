class Solution {
public:
   /* TIMECOMPLEXITY: O(N) SPACE: O(N)
   int majorityElement(vector<int>& nums) {
        unordered_map<int, int>mp;
        int max=nums[0];//store first element as maximum
        
        for(auto x:nums){//store array on map
           mp[x]++; 
        }
        for(auto x: mp){
            if(x.second> mp[max]){//if the count of an element of a map > the max count we change max
                max=x.first;
            }
        }
        
        return max;
    }*/
    
    int majorityElement(vector<int>& nums) {
        int n=nums.size();
        sort(nums.begin(),nums.end());        
        return nums[n/2];
    }
    
    /*int majorityElement(vector<int>& nums) {
        int max=nums[0];//store first element as maximum
        
        
        return max;
    }*/
};