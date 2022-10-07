class Solution {
public:
    int lengthOfLongestSubstring(string s) {
       int n= s.length();
       int c=0, m=0;
        vector<char>v;
        vector<char>::iterator it,it1;
        for(int i=0; i<n; i++){
          it=find(v.begin(), v.end(), s[i]);
            if(it!=v.end()){
               int count =1;
                it1=v.begin();
                while(it1!=it){
                    it1++;
                    count++;
                }
                if(it==v.begin()) v.erase(it);
                else v.erase(v.begin(), ++it);
               v.push_back(s[i]);
                c++;
                c-=count;
            } 
            else{
                v.push_back(s[i]);
                c++;
            }
            m= max(m,c);
        }
        return m;
    }
};