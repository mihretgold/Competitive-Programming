/*class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) { 
        priority_queue<int>p(nums.begin(),nums.end());// orders the elements in inreasing order
       vector<int>v;
        while(!p.empty()){
            v.push_back(p.top());// puts the elements in deacreasing order 
            p.pop();// pops the pushed elements so the next element can be pushed
        }
        int ans=v[k-1];//the (k-1)th index holds the kth largest element
        return ans;
    }
};*/


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) { 
       priority_queue<int,vector<int>, greater<int>>p;
        for(int x: nums){
            //check if size of p is < k
           if(p.size()<k){
              p.push(x); 
           } 
            else{
                 if(p.top()<x){//if size > k and x>p.top()
                     p.pop();// replace the element
                     p.push(x);
                 }
            }
        }
        return p.top();
    }
};