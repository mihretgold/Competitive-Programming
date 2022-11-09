class Solution {
public:
    /*vector<int> pancakeSort(vector<int>& arr) {
       vector<int> ans;
        //almost like bubble sort
        for (int i = arr.size()-1; i > 0; --i) {
            for (int j = 1; j <= i; ++j){//we start j from 1 so that it skips if the number is on the right spot
                if(arr[j]==i+1){//since the max num == the size of the array or i+1
                    reverse(arr.begin(),arr.begin()+j);//when we find the max we flip it to the front
                    ans.push_back(j+1);
                    break;
                }
            }
             reverse(arr.begin(),arr.begin()+i);// then we flip the whole thing bring it to the end
             ans.push_back(i+1); 
        }
        return ans;  */
        /* vector<int> pancakeSort(vector<int>& arr) {
        vector<int>ans;
        for(int i = arr.size() - 1;i>=0; i--){
            if(arr[i] != i+1){
                //Find i+1
                int j = 0;
                while(arr[j] != i+1) j++;
                //Reverse 0,j
                ans.push_back(j+1);reverse(arr.begin(),arr.begin()+j);
                
                //Reverse 0,i
                reverse(arr.begin(),arr.begin()+i);ans.push_back(i+1);
            }
        }
        return ans;*/
     void reverse(int l,int r,vector<int>&arr){
        while(l < r){
            swap(arr[l],arr[r]);
            l++;r--;
        }
    }
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int>res;
        for(int i = arr.size() - 1;i>=0; i--){
            if(arr[i] != i+1){
                //Find i+1
                int k = 0;
                while(arr[k] != i+1) k++;
                //Reverse 0,k
                res.push_back(k+1);reverse(0,k,arr);
                
                //Reverse 0,i;
                reverse(0,i,arr);res.push_back(i+1);
            }
        }
        return res;
    }
};
