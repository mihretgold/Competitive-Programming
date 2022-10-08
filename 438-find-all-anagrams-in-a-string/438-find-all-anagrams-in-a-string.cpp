class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
      vector<int> ans;
      vector<int>ph(26,0);
      vector<int>h(26,0);
        int w=p.size();
        int n=s.size();
        int l=0, r=0;
        if(n<w)
            return ans;
        
        while(r<w){
            ph[p[r]-'a']+=1;
            h[s[r++]-'a']+=1;
        }
        r--;
        while(r<n){
            if(ph == h)
                ans.push_back(l);
                r++;
            if(r!=n)
                h[s[r]-'a']+=1;
                h[s[l]-'a']-=1;
            l++;
        }
        return ans;
    }
};