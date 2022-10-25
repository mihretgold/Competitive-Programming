class Solution {
public:
    /*
    Algorithm
    1)declare a vector to hold the max index of the letters and an ans vector
    2) declare 2 ptrs
    3) store the max occurance of each letter
    4) find the max occurance of the range
    5) then put the size in a vector 
    6) then let the left ptr start again after the last range
    
    
    */
    vector<int> partitionLabels(string s) {
      vector<int> idx(26,0);
        vector<int>v;
        int n=s.size(),l=0,r=0;
        for(int i=0; i<n; i++)
            idx[s[i]-'a']=i; //Holds the end of index for each letter by updating it with the max if it occurs again 
        
        for(int i=0; i<n; i++){
            r=max(r,idx[s[i]-'a']);//puts r ptr to max range
            if(i==r){//all char of current partition are included
               v.push_back(i -l+1);
                l= i+1;
            }
            
        }
        
        return v;
    }
};