class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
     vector<int> v(26);
      for(auto ch : tasks){
         v[ch-'A']++; 
      } 
        int max_cnt=0;
        int max_tsks=0;
        for(int i=0;i<26;++i){
            if(v[i]>max_cnt){
                max_tsks=1;
                max_cnt = v[i];
            }
            else if(v[i]==max_cnt){
                max_tsks++;
            }
        }
        int ans = (max_cnt-1)*(n+1)+(max_tsks);
        return ans>tasks.size()?ans:tasks.size();
    }
};