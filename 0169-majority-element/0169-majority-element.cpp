class Solution {
public:
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
    }
};