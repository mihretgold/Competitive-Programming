class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
     unordered_map<int,long>m;
        int mod=1e9 +7;
        
        for(int x : arr) m[x]++;
        long ans=0;
        for(auto x: m)
            for(auto y:m){
                int i=x.first, j=y.first, k=target -i -j;
                if(!m.count(k)) continue;
                if( i== j && j==k)
                ans += m[i] * (m[i]-1) * (m[i]-2)/6;
                else if(i == j && j!=k)
                 ans += m[i] * (m[i]-1)/2*m[k];   
                else if(i<j && j<k)
                   ans += m[i] * m[j] * m[k];     
            }
        return ans % mod;
    }
};