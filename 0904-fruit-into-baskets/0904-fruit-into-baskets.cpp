class Solution {
public:
    /*
    556698111222   count =2
                  
   max(j-i)
   max(j-i+1)
    */
    int totalFruit(vector<int>& fruits) {
     unordered_map<int,int>mp;
        int n=fruits.size();
        int i=0,j, m=0;
        for(j=0; j<n; j++){
            mp[fruits[j]]++; //adding to map
            while(mp.size()>2){// check if fruits > 2               
                if(--mp[fruits[i]]==0) mp.erase(fruits[i]); //erase both the counts and the elements
                i++;
            }   
             m=max(m,j-i+1);
        }
        return m;
    }
};

