class Solution {
public:
    int maxCoins(vector<int>& piles) {
      int n=piles.size(),sum=0,counts=0;
        sort(piles.begin(),piles.end());
        //we do n/3 to leave 1/3 of the elements to bob and iterate the rest 2/3 with Alison
        for(int i=n/3; i<n; i+=2){
            sum+=piles[i];
        }
        return sum;
       
    }
};