class Solution {
public:
    /*
    0123456789   111
    cbaebabacd   abc 
               
    
    */
    vector<int> findAnagrams(string s, string p) {
     vector<int>mp(26,0); //count of anagram
     vector<int>m(26,0);//count of s
     vector<int>ans;//for index
        int n=s.size(),l=0,r=0;
        int len=p.size();
        if(n<len)return ans;//if size of anagram < string we retrun an empty string
        
        while(r<len){//for the length of the anagram
            mp[p[r]-'a']++;//add count of anagram
            m[s[r++]-'a']++;//add elements until size of anagram
        }
        r--;
        while(r<n){
             if(mp==m){//check if an anagram
                 ans.push_back(l);
               }
                 r++;
             
             if(r!=n){ // to fix overflow problem
                  m[s[r]-'a']++;
                  m[s[l]-'a']--;
              }
                l++;
          } 
        return ans;
    }
};