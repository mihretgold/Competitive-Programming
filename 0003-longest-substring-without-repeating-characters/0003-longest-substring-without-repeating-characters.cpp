class Solution {
public:
    /*
    "abcabcbb"
        ^  ^
      i,j
      hash map >1
      find index +1
    
    */
    int lengthOfLongestSubstring(string s) {
       int i,ans=0,x=0,y=0;
        for(int j=0;j<s.size();j++)// iterates through string
        {
            
            for(i=x;i<j;i++) // if i<j iterates to check any simillar elements
            {
            // if similar elements are found increaments the starting index of i to start from the found element+1
                if(s[i]==s[j])
                {
                    y=i+1;  
                }
            }
              ans=max(ans,j-y+1); 
            x=y;
          
        }
        return ans;
    }
};
