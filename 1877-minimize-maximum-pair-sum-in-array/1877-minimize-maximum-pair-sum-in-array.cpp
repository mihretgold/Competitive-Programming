class Solution {
public:
    int minPairSum(vector<int>& v) {
         int s=0, e=v.size()-1;
    int maxi=0,sum;
    //to find minimized max pair sum
    sort(v.begin(),v.end());
    while(s<e){
        sum=v[s]+v[e];
        maxi=max(maxi,sum);
        s++;
        e--;
    }
    
    return maxi; 
    }
};