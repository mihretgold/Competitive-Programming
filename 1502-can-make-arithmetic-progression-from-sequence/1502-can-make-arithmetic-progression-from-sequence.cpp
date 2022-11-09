class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        int i;
        sort(arr.begin(),arr.end());
        for( i=2; i<arr.size(); i++){
            if(arr[i]-arr[i-1]!= arr[1]-arr[0])
                break;
        }
        return i==arr.size();
    }
};