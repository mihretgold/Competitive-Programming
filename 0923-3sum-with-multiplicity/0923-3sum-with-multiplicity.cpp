class Solution {
public:
    /*
    Algorithm 
    1) declare a hash map
    2) put count of each on hashmap
    3) make a nested loop for i & j that iterates over a map(range based)
    4) declare variables to put the elements of the map in ans declare k as target -i-j
    5) if k is not found countinue
    6) if all the elements are the same multiply use the count of one and decreament 1 then 2 from it then divide it with 3 factorial(6)
    7) if 2 of the elements are the  same  multiply the count and -1 of the same numbers and multiply the count of the distnict number then divide it by 2 factorial(2)
    8)if all of the elements are d/f simply multiply thier counts
    9) return ans % 1e9 +7(10^9 +7)
    
    
    
    */
    int threeSumMulti(vector<int>& arr, int target) {
     unordered_map<int,long>m;
        int mod=1e9 +7;
        
        for(int x : arr) m[x]++;//put count of each on hashmap
        long ans=0;
        for(auto x: m)//x loop for i
            for(auto y:m){//y loop for j
                int i=x.first, j=y.first, k=target -i -j;//put the elements from the map to a variable
                if(!m.count(k)) continue;//if k is no found
                if( i== j && j==k)// if all the elements are the same
                ans += m[i] * (m[i]-1) * (m[i]-2)/6;
                else if(i == j && j!=k)//if 2 of the elements are the  same
                 ans += m[i] * (m[i]-1)/2 * m[k];   
                else if(i<j && j<k)//if all are diffrent and less than each other
                   ans += m[i] * m[j] * m[k];     
            }
        return ans % mod;
    }
};