class Solution {
public:
    void rotate(vector<int>& nums, int k) {
     int n=nums.size();
        k%=n;//for when k>n   
        reverse(nums.begin(), nums.begin()+n-k);//from[1,2,3,4,5,6,7]-> [4,3,2,1,5,6,7]
        reverse(nums.begin()+n-k, nums.end());//from [4,3,2,1,5,6,7] -> [4,3,2,1,7,6,5]
        reverse(nums.begin(), nums.end());//from  [4,3,2,1,7,6,5] -> [5,6,7,1,2,3,4]
    }
        
};