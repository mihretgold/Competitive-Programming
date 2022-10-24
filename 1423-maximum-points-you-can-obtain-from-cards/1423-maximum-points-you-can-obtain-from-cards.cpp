class Solution {  
public:
    /*
     0 1 2 3 4 5 6
    [1,2,3,4,5,6,1], k = 3 s=6
    
    */
    /*int maxScore(vector<int>& cardPoints, int k) {
        int n= cardPoints.size();
        int sum=0, curr;
        for(int s =0; s<k; s++) sum+= cardPoints[s];//sum the first k elements
        curr=sum;
        for(int s=k-1; s>=0; s--){//starting from the k-1 index we remove the element and add the element at the end until 0
            curr-=cardPoints[s];
            curr+=cardPoints[n-k+s];
            sum=max(sum,curr);//find max window
        }
        return sum;
    }*/
    int maxScore(vector<int>& cardPoints, int k) {
        int n=cardPoints.size();
        int sum=0,e=n-1,m;
        for(int i=0; i<k; i++)sum+=cardPoints[i];//adds the first k elements
        m=sum;
        for(int i=k-1; i>=0; i--){// check max sum
            m-=cardPoints[i];
            m+=cardPoints[e--];
            sum=max(m,sum);
        }
        return sum;
    }
};