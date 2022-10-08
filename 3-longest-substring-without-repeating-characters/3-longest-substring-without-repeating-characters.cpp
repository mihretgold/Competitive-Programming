class Solution {
public:
    int lengthOfLongestSubstring(string s) {
     int i,j,ans=0,x=0,y=0;
        for( j=0; j<s.size(); j++){
            for(i=x; i<j; i++){
               if(s[i]==s[j]){
                   y=i+1;
               }
                
            }
          
            x=y;
            ans= max(ans,j-y+1);
        }
        
        return ans;
    }
};