class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int>res;
        for(int i = arr.size() - 1;i>=0; i--){
            //since the size of the array is the max number
            if(arr[i] != i+1){//if the last element is not the max num b/c it would already be in it's place
                //Find i+1
                int k = 0;
                while(arr[k] != i+1) k++;//increament k until==i+1
                //Reverse 0,k puting i+1 element to the front
                res.push_back(k+1);reverse(arr.begin(),arr.begin()+k+1);
                
                //Reverse 0,i putting i+1 element at the end
               reverse(arr.begin(),arr.begin()+i+1);res.push_back(i+1);
            }
        }
        return res;
    }
};
