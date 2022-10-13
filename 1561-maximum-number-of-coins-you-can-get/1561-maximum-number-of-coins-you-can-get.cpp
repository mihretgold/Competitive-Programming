class Solution {
public:
    int maxCoins(vector<int>& piles) {
      int n=piles.size(),sum=0,counts=0;
        sort(piles.begin(),piles.end());
        int k=n/3,i=1;
        for(int i=n/3; i<n; i+=2){
            sum+=piles[i];
        }
        return sum;
       
    }
};