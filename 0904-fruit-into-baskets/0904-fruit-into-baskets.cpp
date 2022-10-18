class Solution {
public:
   
    int totalFruit(vector<int>& fruits) {
      unordered_map<int,int>mp;
        int n= fruits.size(), m=0;
       int i=0,j=0;
        
        while(j<n){
            
                mp[fruits[j]]++;
            
            while(mp.size()>2)
            {
                if(mp[fruits[i]]==1)
                {
                    mp.erase(fruits[i]);
                }
                else
                {
                    mp[fruits[i]]--;
                }
                i++;
            }
            
            m=max(m, j-i+1);
            j++;
        }
        
        return m;
    }
};

