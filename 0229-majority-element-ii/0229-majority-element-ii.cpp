class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
       unordered_map<int, int>mp;
        vector<int>ans;
        int n=nums.size();
        for(auto x:nums){//store array on map
           mp[x]++; 
        }
        for(auto x: mp){
            if(x.second> n/3){//if the count of an element of a map > array size/3
                ans.push_back(x.first);
            }
        }
        
        return ans;  
    }
};