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
    /* TIMECOMPLEXITY: O(NlogN) SPACE: O(1)   
    int majorityElement(vector<int>& nums) {
        int n=nums.size();
        sort(nums.begin(),nums.end());        
        return nums[n/2];
    }*/
     //TIMECOMPLEXITY: O(N) SPACE: O(1)  
    int majorityElement(vector<int>& nums) {
        int n=nums.size();
        int max=nums[0],count=1;//store first element as max and start count as 1
        for(int i=1; i<n; i++){
            if(max==nums[i]){//if next element is same as max increament count
                count++;
            }else if(count==0){//if count becomes 0 store the element as max and increament count
                count++;
                max=nums[i];
            }else{//if next element is not equal to max deacreament count
                count--;
            }
        }
        
        return max;
    }
};