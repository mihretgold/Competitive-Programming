class Solution {
public:
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