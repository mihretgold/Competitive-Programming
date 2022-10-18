class Solution {  
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n= cardPoints.size();
        int sum=0, curr;
        for(int s =0; s<k; s++) sum+= cardPoints[s];
        curr=sum;
        for(int s=k-1; s>=0; s--){
            curr-=cardPoints[s];
            curr+=cardPoints[n-k+s];
            sum=max(sum,curr);
        }
        return sum;
    }
};