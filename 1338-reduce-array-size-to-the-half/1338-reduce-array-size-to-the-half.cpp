class Solution {
public:
    static bool cmp(pair<int,int>&a ,pair<int,int>&b){
            return a.second>b.second;//sort in decreasing order
    }
    
    int minSetSize(vector<int>& arr) {
     unordered_map<int,int>m;
      int n=arr.size();
      int counts=0,sum=0,i=0;
       
        for(auto i: arr){//add nums and count to map
            m[i]++;
        }
         vector<pair<int,int>>v(m.begin(),m.end());//copy map to vector to sort
   
        sort(v.begin(), v.end(),cmp);//sort according to count
        
        while(sum <n/2){//add counts of element till it becomes >= n/2
            sum+=v[i].second;
            counts++;
            i++;
        }          
        
        return counts;
    }
};