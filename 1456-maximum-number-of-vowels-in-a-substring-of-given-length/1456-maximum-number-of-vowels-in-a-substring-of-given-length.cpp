class Solution {
public:
    int maxVowels(string s, int k) {
      int n=s.length();
      int l=0, r=0,counts=0,m=0;
        while(r<n){
            if(s[r]=='a'||s[r]=='e'||s[r]=='i'||s[r]=='o'||s[r]=='u'){
                counts++;
            }
            if(r-l+1 >k){
                if(s[l]=='a'||s[l]=='e'||s[l]=='i'||s[l]=='o'||s[l]=='u'){
                counts--;
                }
                l++;
            }
            r++;
            m=max(m,counts);
        }
        return m;
    }
};