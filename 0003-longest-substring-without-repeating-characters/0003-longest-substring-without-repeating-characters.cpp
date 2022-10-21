class Solution {
public:
    /*
    "abcabcbb"
        ^  ^
      i,j
      hash map >1
      find index +1
     1) Brute force apprach 
    "abcabcbb"
      ^   ^
   i=0 j=0 y=0  ans=1
   i=1 j=0 y=0  ans=2 
   i=2 j=0 y=0  ans=3 
   i=3 j=0 y=1  ans=3 
   i=4 j=1 y=2  ans=3 ...
   
       i,j,ans, y=0

    
    */
    /*
    Algorithm
    1) nested loop with first loop iterating through the sring
    2) And the second loop searching for duplicate elements
    3) start the second loop from the found element + 1 or zero until dulicate element is found
    4) inside loops if duplicate is found from 0(found e+1) to < element j is at the iteration of the 1st loop
    5)after the second loop calculate max sub array
    
    */
   /* int lengthOfLongestSubstring(string s) {
       int i,ans=0,y=0;
        for(int j=0;j<s.size();j++)// iterates through string
        {
            
            for(i=y;i<j;i++) // if i<j iterates to check any simillar elements
            {
            // if similar elements are found increaments the starting index of i to start from the found element+1
                if(s[i]==s[j])
                {
                    y=i+1;  
                }
            }
              ans=max(ans,j-y+1); //puts max subarray to ans variable          
        }
        return ans;
    }*/
    /*
   int lengthOfLongestSubstring(string s) {
        int i=0, j=0, maxlen=0, len=0;
        unordered_map<char,int> mymap;
        while(j<s.length()){
            if(mymap[s[j]]>0){
                len = j-i;
                maxlen = max(maxlen, len);
                while(s[j]!=s[i]){
                    mymap[s[i]]--;
                    i++;
                }mymap[s[i]]--;
                 i++;
            }else if(j==s.length()-1){
                len = j-i+1;
                maxlen = max(maxlen, len);
            }
            mymap[s[j]]++;
            j++;
        }
        return maxlen;
    }*/
    
 /* int lengthOfLongestSubstring(string s) {
     unordered_map<char, int> m; //character map to index
     int maxi = 0, l = 0, r = 0;
     
     while (r < size(s)) {
         if (m.find(s[r]) == m.end() || m[s[r]] < l) //element not in window!
             maxi = max(maxi, r-l+1);
         else  l = m[s[r]] + 1;//element in window
         m[s[r++]] = r; //update element in map, and increment r;
     }
     return maxi;
 }*/
    int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (int i = 0; i != s.length(); i++) {
            if (dict[s[i]] > start)
                start = dict[s[i]];
            dict[s[i]] = i;
            maxLen = max(maxLen, i - start);
        }
        return maxLen;
    }
    
    
    
};
