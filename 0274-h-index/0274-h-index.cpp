class Solution {
public:
    /*
     [3,0,6,1,5]     [1,3,1]
     
     [01356] sort    113 
     check if n-e=e  
     check index=n-e
     m
    
    */
    int hIndex(vector<int>& citations) {
        int n=citations.size(),count=0;
        sort(citations.begin(),citations.end());//sort the nums so we can use the indexes to calculate the elements > and <
        for(int i=n-1; i>=0; i--){//start from largest element
            if(n-i<=citations[i])//check indexes from the back
                count++;
        }
        return count;
    }
};